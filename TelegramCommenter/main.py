
from telethon import TelegramClient, events, errors
import telegram

from random import choice, choices
from datetime import datetime
from time import time
import configparser
import getpass
import asyncio
import os



asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
config = configparser.ConfigParser()
config.read(os.path.abspath('config.cfg'))

api_id = int(config['Settings']['api_id'])
api_hash = config['Settings']['api_hash']
phone = config['Settings']['phone']
password = config['Settings']['password']
password = password if password.strip() else lambda: getpass.getpass('Please enter your password: ')
session_name = config['Settings']['session_name']

bot_token = config['Settings']['bot_token']
admin_user_id = config['Settings']['admin_user_id']
channel_msg_delay = int(config['Settings']['channel_msg_delay'])

text_file = config['Data']['text_file']
channels_file = config['Data']['channels_file']


def get_random_text():
    text = choice(text_list).strip()
    text = choices([text, text.title()], weights=[0.7, 0.3])[0]
    return text.strip()

def get_data():
    for path in [text_file, channels_file]:
        if not os.path.exists(os.path.abspath(path)):
            print(f'{datetime.now():%Y-%m-%d %H:%M:%S} - Wrong file path [{os.path.abspath(path)}]')
            os._exit(0)

    with open(os.path.abspath(text_file), 'r', encoding='utf-8') as f:
        text_list = [l.strip() for l in f]

    with open(os.path.abspath(channels_file), 'r', encoding='utf-8') as f:
        channels_id = []
        for l in f:
            l = l.strip()
            if l.replace('-', '').isdigit():
                channels_id.append(int(l))
            else:
                channels_id.append(l)
    return text_list, channels_id

if not bot_token.strip() or not admin_user_id.strip():
    bot = False
else:
    bot = telegram.Bot(token=bot_token)
client = TelegramClient(session_name, api_id, api_hash)
client.start(phone=phone, password=password)
text_list, channels_id = get_data()
channels_data = {}
print(f'{datetime.now():%Y-%m-%d %H:%M:%S} - Bot Succesfully started work')

@client.on(events.NewMessage(chats=channels_id))
async def handle_new_message(event):
    text = get_random_text()
    entity = await client.get_entity(event.chat_id)

    if not event.message.message:
        return
    if event.chat_id not in channels_data:
        channels_data[event.chat_id] = None
    if channels_data[event.chat_id] is not None:
        if time() - channels_data[event.chat_id] < channel_msg_delay:
            return

    if entity.username is None:
        message_url = f"https://t.me/c/{event.message.input_chat.channel_id}/{event.message.id}"
    else:
        message_url = f"https://t.me/{entity.username}/{event.message.id}"

    try:
        await client.send_message(event.chat_id, text, comment_to=event.message.id)
        status = 'Success'
        channels_data[event.chat_id] = time()
    except errors.rpcerrorlist.MsgIdInvalidError:
        status = 'Chat unavailable'
    except errors.ChannelPrivateError:
        status = 'Chat unavailable'
    except Exception as e:
        status = str(e)

    bot_text =f'''-=- New message in channel ({event.message.id})
-=- Time: {datetime.now():%H:%M:%S}
-=- Text: {event.message.text}
-=- Url: <a href="{message_url}">{entity.title}</a>
-=- Bot response: {text}
-=- Status: {status}'''
    print(bot_text.replace('<a href="', '').replace('</a>', '').replace('">', ' | ') + '\n')
    if bot is not False:
        await bot.send_message(chat_id=admin_user_id,
                               text=bot_text, parse_mode='HTML', disable_web_page_preview=True)

client.run_until_disconnected()