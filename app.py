from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('kVF6UJaZuLMvh/dwcy5HfSUMkFsEBXxgznLtyJJbQT0zuhlgFTGHN0j1K8LDTLbQIglwyxS7tEn/CEEg4j9BashuePYvBrpkgvfcT6ZqzzGIdXaMBZ3QgTxpbBX1ixfiryDkRWbpsHe452xlHuSJswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e5573fef470e27156a9325fd225a4f16')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = 'Have you eaten?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()