import datetime

from bothandler import BotHandler
from private import token

bot = BotHandler(token)
now = datetime.datetime.now()

print( 'started')
print(now)

def show_help():
            assert isinstance(bot, object)
            bot.send_message(last_chat_id, 'По всем вопросам обращаться к @irisinlovee')

def message_handle(message):
    if message == '/help':
       show_help()


def main():
    new_offset = None

    while True:
        bot.get_updates(new_offset)

        last_update = bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        bot.send_message(last_chat_id, message_handle(last_chat_text))

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
