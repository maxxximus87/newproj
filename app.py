from flask import Flask, request, abort

from linebot import (
LineBotApi, WebhookHandler
)

from linebot.exceptions import (
InvalidSignatureError
)
from linebot.models import (
MessageEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('lansQdWVzGr0yWaVWk4SN/V6ZMsTFAILRAudOfM7BAgtaYTopXa9du2KBCsEgVXqINOBDW4AUpWh50OJN1n9fq6pwWNP9sxeL0v03LTi242pik8n8UcdfrSiuapsgIsasHNLkeuF5bp+TkgdjaPCPgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f937d4f3b0187f6f1d36ea87ff080c44')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello World!")
    )


if __name__ == "__main__":
    app.run()