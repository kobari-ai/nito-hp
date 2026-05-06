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
    formatPhoneCellAsText_(sheet, sheet.getLastRow(), payload.phone);

    // Slack 通知（スクリプトのプロパティ SLACK_INCOMING_WEBHOOK_URL が未設定なら何もしない）
    try {
      notifySlackIncomingWebhook_(payload);
    } catch (slackErr) {
      // シート保存は成功させる（通知失敗でフォーム送信をエラーにしない）
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

/**
 * Incoming Webhook で Slack に通知する。
 * プロジェクトの「スクリプトのプロパティ」に SLACK_INCOMING_WEBHOOK_URL を設定すること。
 * https://api.slack.com/messaging/webhooks
 */
function notifySlackIncomingWebhook_(payload) {
  var url = PropertiesService.getScriptProperties().getProperty("SLACK_INCOMING_WEBHOOK_URL");
  if (!url) {
    return;
  }

  var msg =
    "*お問い合わせが届きました*\n" +
    "• 氏名: " + (payload.name || "") + "\n" +
    "• 会社: " + (payload.company || "") + "\n" +
    "• 部署: " + (payload.department || "") + "\n" +
    "• メール: " + (payload.email || "") + "\n" +
    "• 電話: " + (payload.phone != null ? String(payload.phone) : "") + "\n" +
    "• カテゴリ: " + (payload.category || "") + "\n" +
    "• 内容: " + truncateForSlack_(payload.message || "", 800);

  var body = {
    text: msg,
    unfurl_links: false,
    unfurl_media: false
  };

  UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(body),
    muteHttpExceptions: true
  });
}

function truncateForSlack_(text, maxLen) {
  if (text.length <= maxLen) {
    return text;
  }
  return text.substring(0, maxLen) + "…（省略）";
}
