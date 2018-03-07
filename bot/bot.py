from urllib.parse import urlparse

import flask
from telebot import TeleBot, types

from config import TOKEN, server, db

from aggregator import User

bot = TeleBot(TOKEN)
app = flask.Flask(__name__)
APP_URL = f"https://{server.public_host}:{server.port}"

# base skeleton of bot app
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''

@app.route(f"/{TOKEN}", methods=['POST'])
def web():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


@bot.message_handler(commands=['start'])
def hello(msg):
    # init user and create document of this user in database
    User(msg.chat.id)


@bot.message_handler(content_types=['text'])
def check_link(msg):
    user = User(msg.chat.id)
    splitted_text = msg.text.split()
    if urlparse(splitted_text[0]).netloc:
        bot.send_message(
            user.user_id,
            user.create_link(splitted_text[0], splitted_text[1:]))
    else:
        user.get_links_by_tags(splitted_text)


if __name__ == "__main__":
    bot.remove_webhook()

    bot.set_webhook(
        url=f"{APP_URL}/{TOKEN}",
        certificate=open(server.cert))
    app.run(host=server.host,
            port=server.port,
            ssl_context=(server.cert, server.pkey),
            debug=True)