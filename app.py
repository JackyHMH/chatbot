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

line_bot_api = LineBotApi('Ov9IEh+zR2oFbNB8M4ezNsnJNu+kXBng+STE3vDKfLmU5w3Tl9nEQi3yEep3rpE77jbW0/dj2SIOysdfwpGTIKyQxrA4pUJRgNog3xiIS7lv1tCN/qjKBJeDLLi0OYCxdAIedgtdChyR3cIZ9DWmfAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('99bc3be057b18db0da151beb8d6ebf46')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)99bc3be057b18db0da151beb8d6ebf46

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()