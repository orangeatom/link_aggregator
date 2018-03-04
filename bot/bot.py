import flask
from telebot import TeleBot, types

from config import TOKEN, server, db

from aggregator import check_message

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
    pass


@bot.message_handler(content_types=['text'])
def check_link(msg):
    pass


if __name__ == "__main__":
    bot.remove_webhook()

    bot.set_webhook(
        url=f"{APP_URL}/{TOKEN}",
        certificate=open(server.cert))
    app.run(host=server.host,
            port=server.port,
            ssl_context=(server.cert, server.pkey),
            debug=True)