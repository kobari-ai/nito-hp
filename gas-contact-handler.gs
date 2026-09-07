/**
 * 権限承認＆Slack通知の動作確認用。
 * 末尾に _ を付けない＝GASエディタの実行メニューに表示される。
 * ここから1回実行して承認すると、UrlFetchApp などの権限が付与される。
 */
function runAuthorizationAndTestSlack() {
  var url = PropertiesService.getScriptProperties().getProperty('SLACK_WEBHOOK_URL');
  Logger.log('SLACK_WEBHOOK_URL: ' + (url ? '設定あり' : '★未設定'));
  testNotifySlack_();
  Logger.log('完了しました。Slackにテスト通知が届いていれば成功です。');
}

function testNotifySlack_() {
  notifySlack_({
    name: 'テスト太郎',
    company: 'テスト株式会社',
    email: 'test@example.com',
    phone: '09012345678',
    category: 'テスト通知',
    site_url: 'https://example.com',
    message: 'これはSlack通知の単体テストです。'
  });
}

function doPost(e) {
  try {
    // スプレッドシートIDはURLの /d/ と /edit の間の文字列
    // シート（タブ）名はスプレッドシート側の名前と完全一致させる（例: お問い合わせ）
    var sheet = SpreadsheetApp.openById("1FV6mztN-8h25bdugC0XWM760YvoQa7W-HKCZDEAzX14").getSheetByName("お問い合わせ");
    if (!sheet) {
      throw new Error("Sheet 'お問い合わせ' not found.");
    }

    var HEADERS = [
      "受信日時",
      "氏名",
      "会社名",
      "部署名",
      "勤務先メール",
      "電話番号",
      "業務における立場",
      "立場（その他）",
      "対策サイトURL",
      "nitoを知ったきっかけ",
      "きっかけ（その他）",
      "ご相談カテゴリ",
      "ご相談内容"
    ];

    var payload = JSON.parse(e.postData.contents || "{}");

    var row = [
      new Date(),
      payload.name || "",
      payload.company || "",
      payload.department || "",
      payload.email || "",
      payload.phone || "",
      payload.role || "",
      payload.role_other || "",
      payload.site_url || "",
      payload.referral || "",
      payload.referral_other || "",
      payload.category || "",
      payload.message || ""
    ];

    ensureHeaderRow_(sheet, HEADERS);

    sheet.appendRow(row);

    // 電話番号は数値扱いされると先頭の0が落ちるため、文字列として上書きする（列6＝F）
    // Slack通知より先に実行する。通知が失敗しても電話番号が壊れないようにするため。
    formatPhoneCellAsText_(sheet, sheet.getLastRow(), payload.phone);

    // Slack通知の失敗でフォーム送信を失敗扱いにしない（保存はすでに完了しているため）
    try {
      notifySlack_(payload);
    } catch (slackErr) {
      console.error('Slack通知に失敗: ' + slackErr);
    }

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(error) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * 1行目が見出し（受信日時）でなければ、上に行を挿入して見出しを書く。
 * 完全に空のシートなら見出し行だけ先に足す（次の appendRow がデータ行になる）。
 */
function ensureHeaderRow_(sheet, headers) {
  var lastRow = sheet.getLastRow();
  if (lastRow === 0) {
    sheet.appendRow(headers);
    return;
  }
  var a1 = sheet.getRange(1, 1).getValue();
  if (a1 === "受信日時") {
    return;
  }
  sheet.insertRowBefore(1);
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
}

/** 電話番号列を「文字列」表示にし、先頭の0を保持する */
function formatPhoneCellAsText_(sheet, row, phone) {
  var phoneCol = 6;
  var cell = sheet.getRange(row, phoneCol);
  cell.setNumberFormat("@");
  cell.setValue(phone != null ? String(phone) : "");
}

function notifySlack_(payload) {
  // URLはコードに直書きせず「プロジェクトの設定 > スクリプト プロパティ」に置く。
  // キー名: SLACK_WEBHOOK_URL（未設定なら通知だけスキップし、保存は成功させる）
  const url = PropertiesService.getScriptProperties().getProperty('SLACK_WEBHOOK_URL');
  if (!url) {
    console.warn('SLACK_WEBHOOK_URL が未設定のため、Slack通知をスキップしました');
    return;
  }

  const message =
    '📩 新しいお問い合わせ\n' +
    `氏名: ${payload.name || ''}\n` +
    `会社名: ${payload.company || ''}\n` +
    `メール: ${payload.email || ''}\n` +
    `電話番号: ${payload.phone || ''}\n` +
    `カテゴリ: ${payload.category || ''}\n` +
    `サイトURL: ${payload.site_url || ''}\n\n` +
    `▼内容\n${payload.message || ''}`;

  const res = UrlFetchApp.fetch(url, {
  method: 'post',
  contentType: 'application/json',
  payload: JSON.stringify({ text: message }),
  muteHttpExceptions: true
});

Logger.log(res.getResponseCode());
Logger.log(res.getContentText());
}