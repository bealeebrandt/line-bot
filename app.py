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

line_bot_api = LineBotApi('bZq3F/rMXgK+hYG/x3uYy46JqppPG+ga6Kiijo7WGwUZ0Orz0rXh1JkzwdssdVCT92Ek3VSOGseVN4JZpJjgcu4WttvVjUphJtg6SA+AypqFU6QfEcSKWXYmNcT8rpSQSkdbSpVzWG5bYidORmZawQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('94f510eb9b7fec9e78cb2b1b56caa09a')


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