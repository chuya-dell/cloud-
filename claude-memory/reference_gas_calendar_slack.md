---
name: reference-gas-calendar-slack
description: Googleカレンダー予定のSlack自動通知システム(GAS + Incoming Webhook)
metadata: 
  node_type: memory
  type: reference
  created: 2026-07-10
  updated: 2026-07-10
  status: active
  tags: 
    - google-apps-script
    - google-calendar
    - slack
    - notification
    - 分析化学研究グループ
  originSessionId: dd50376c-27b1-4e73-8e6f-5cd70daad5ae
---

## summary

Googleカレンダーの予定を毎日自動チェックし、予定がある場合のみSlackへ通知するGAS。完全無料運用。通知は1日2回(前日夕方・当日朝)、予定がない日は送信をスキップしてSlackを汚さない仕様。

## 前提構成

- 使用アカウント: **分析化学研究グループ**アカウント(Google/Slack共通)
- Slack側: Incoming Webhook(Slack Appアプリ名`Google-Calendar-Bot`)
- GAS: 分析化学研究グループのGoogleアカウントに紐づくGASエディタ上に配置

## 仕様(通知タイミングと条件)

- 通知条件: 対象日に予定がある場合のみ送信(予定がない日はスキップ)
- 通知タイミング(1日2回):
  1. 前日の夕方(17:00〜18:00の間、トリガーは16-18時台実行想定): 翌日の予定を「明日の予定(前日通知)」として送信
  2. 当日の朝(9:00〜10:00の間、トリガーは8-10時台実行想定): 当日の予定を「本日の予定」として送信

## current_version(2026-07-10 バグ修正版・適用済み)

```javascript
const SLACK_WEBHOOK_URL = "（GASスクリプトエディタ側の実コードを参照。本ノートには平文記載しない）";
const CALENDAR_ID = "primary"; // メインのカレンダー

function sendCalendarToSlack(){
  const calendar = CalendarApp.getCalendarById(CALENDAR_ID);
  const now = new Date();
  const currentHour = now.getHours();

  // 今日・明日の「日付」だけを持つ基準値(時刻比較で月またぎも正しく判定できるようにする)
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);

  // 当日と翌日の2日分の予定を取得
  const startDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
  const endDate = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 2, 0, 0, 0);
  const events = calendar.getEvents(startDate, endDate);

  let todayMessage = "";
  let tomorrowMessage = "";

  events.forEach(event => {
    const startTime = event.getStartTime();
    const title = event.getTitle();
    // "JST" ではなく正式なIANAタイムゾーンID "Asia/Tokyo" を使用
    const timeStr = event.isAllDayEvent() ? "終日" : Utilities.formatDate(startTime, "Asia/Tokyo", "HH:mm");

    // 予定の「日付」だけを取り出して比較(月またぎでも正しく判定される)
    const eventDate = new Date(startTime.getFullYear(), startTime.getMonth(), startTime.getDate());

    if (eventDate.getTime() === today.getTime()) {
      todayMessage += `・ ${timeStr} 〜 : ${title}\n`;
    } else if (eventDate.getTime() === tomorrow.getTime()) {
      tomorrowMessage += `・ ${timeStr} 〜 : ${title}\n`;
    }
  });

  let finalMessage = "";

  // 朝（9時台想定）の実行なら「当日の予定」をチェック
  if (currentHour >= 8 && currentHour <= 10) {
    if (todayMessage) {
      finalMessage = `*【本日の予定】*\n${todayMessage}`;
    }
  }
  // 夕方（17時台想定）の実行なら「明日の予定」をチェック
  else if (currentHour >= 16 && currentHour <= 18) {
    if (tomorrowMessage) {
      finalMessage = `*【明日の予定（前日通知）】*\n${tomorrowMessage}`;
    }
  }

  // メッセージがある場合（予定が存在する場合）のみSlackに送信
  if (finalMessage) {
    const payload = { "text": finalMessage };
    const options = {
      "method": "post",
      "contentType": "application/json",
      "payload": JSON.stringify(payload)
    };
    UrlFetchApp.fetch(SLACK_WEBHOOK_URL, options);
  }
}
```

## メンテナンス方法

- 通知先Slackチャンネルを変更したい場合: 分析化学研究グループのアカウントでSlack API画面(`https://api.slack.com/apps`)にアクセスし、新しいWebhook URLを発行してコード1行目の`SLACK_WEBHOOK_URL`を書き換える
- 通知する時間を変更したい場合: GASの左メニュー「時計マーク(トリガー)」から登録されている2つのトリガーの時刻を変更し、同時にコード内の時間判定(`currentHour`の条件分岐部分)の数字も合わせる

## 設計上のポイント(重要)

- **Googleカレンダー側の通知/リマインダー設定(○日前通知など)はこのシステムの動作に一切影響しない**。`calendar.getEvents()`で指定範囲の予定を全件取得しているだけで、個々の予定のリマインダー設定は参照していない。通知タイミングはGAS側のtime-driven trigger(2本: 朝用・夕方用)のみで制御される。
- 同一判定・送信可否は「予定の有無」のみで判断(空メッセージなら送信スキップ)。

## resolved_issues(2026-07-10 修正・適用済み)

1. **月またぎバグ(解消)**: 旧コードは`startTime.getDate() === now.getDate() + 1`で判定しており、月末(例: 7/31→8/1)で不成立になり前日通知が翌月初日の予定を拾えなかった。`Date`オブジェクトを日付単位で生成し`getTime()`比較する方式に変更して解消。
2. **タイムゾーン文字列(解消)**: `Utilities.formatDate(startTime, "JST", "HH:mm")`の`"JST"`は正式なIANAタイムゾーンIDでなかった。`"Asia/Tokyo"`に修正済み。

## next_action

- 特になし(修正版を貼り替え・適用済み。問題発生時に見直し)
- 2026-07-10、本ノートに平文記載されていたSlack Webhook URLを伏字化・削除済み(実体はGASスクリプトエディタ側のコードで管理。再確認・再発行が必要な場合はSlack API画面から)

## related

- [[reference_gas_drive_sync]] — 同じくGASベースの自動化(Google Drive一方向同期)
