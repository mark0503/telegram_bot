import telebot
from telebot import types
import keyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, update
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import pprint

import collections


dic = {}
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1uKw1k7Acj_9ToYVxDs42t_pdshl0vOG5uTNQPMyQe8w'

token = '1704249879:AAEYWSZcpgJU15JegqJDsEkjgRacIoTlJ-Y'
bot = telebot.TeleBot(token)


credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.from_user.username in dic:
        iid = dic[message.chat.username]
        iid = iid['num']
        name = message.from_user.first_name
        keyboard = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="My Data", callback_data='Data')
        keyboard.add(url_button1)
        WELCOME_MESSAGE = f"""
        <b>Thank you {name}!</b>

    Don't forget to:
    🔸️ Stay in the telegram channels
    Your personal number is {iid}.
        """
        bot.send_message(
            message.from_user.id,
            WELCOME_MESSAGE,
            parse_mode='html',
            disable_web_page_preview=True,
            reply_markup=keyboard,
        )
    else:
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="✅ Join Airdrop", callback_data='Click')
        keyboard.add(url_button)
        name = message.from_user.first_name
        WELCOME_MESSAGE = f"""
        <b>Hello, {name}! I am your friendly Smarabu-Safemars Airdrop bot.</b>

    ✅Please do the required tasks to be eligible to get airdrop tokens.

    295,000,000 Safemars will be droped.
    How many people will get this tokens we will decide through a survey in the group.
    Click "Join Airdrop" to proceed.
        """
        bot.send_message(
            message.from_user.id,
            WELCOME_MESSAGE,
            parse_mode='html',
            disable_web_page_preview=True,
            reply_markup=keyboard,
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith('Click'))
def longname(call):
    if call.data == 'Click':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="📘 Submit my details", callback_data='Submit')
        keyboard.add(url_button)
        WELCOME_MESSAGE = f"""
🔹️ Total to earn per participant (will decide through a survey)

📢 Airdrop Rules

✏️ Mandatory Tasks:
🔹️ Join this Airdrop announcement  telegram channel
🔹️Join my FREE Airdrops & signals telegram channel
        """
        bot.send_message(
            call.message.chat.id,
            WELCOME_MESSAGE,
            parse_mode='html',
            disable_web_page_preview=True,
            reply_markup=keyboard
            
        )

@bot.callback_query_handler(func=lambda call: call.data.startswith('Submit'))
def next_stap(call):
    if call.data == 'Submit':
        if call.message.chat.username in dic:
            iid = dic[call.message.chat.username]
            iid = iid['num']
            name = call.message.chat.first_name
            keyboard = types.InlineKeyboardMarkup()
            url_button1 = types.InlineKeyboardButton(text="📝 My data", callback_data='Data')
            keyboard.add(url_button1)
            WELCOME_MESSAGE = f"""
            <b>Thank you {name}!</b>

        Don't forget to:
        🔸️ Stay in the telegram channels
        Your personal number is {iid}.
            """
            bot.send_message(
                call.message.chat.id,
                WELCOME_MESSAGE,
                parse_mode='html',
                disable_web_page_preview=True,
                reply_markup=keyboard,
            )
        else:
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="❗️Join now❗️", url='https://t.me/joinchat/KZZmGyKBR802MjQy')
            url_button1 = types.InlineKeyboardButton(text="✅ Done", callback_data='Done')
            keyboard.add(url_button, url_button1)
            WELCOME_MESSAGE = f"""
            🔹️ Join this Airdrop announcement  telegram channel.
Press "Join now" and then "Done" to check.
            """
            bot.send_message(
                call.message.chat.id,
                WELCOME_MESSAGE,
                parse_mode='html',
                disable_web_page_preview=True,
                reply_markup=keyboard
                
            )

CHAT_ID = -1001283920459

@bot.callback_query_handler(func=lambda call: call.data.startswith('Done'))
def longname(call):

    if call.data == 'Done':

        if call.message.chat.username in dic:
            iid = dic[call.message.chat.username]
            iid = iid['num']
            name = call.message.chat.first_name
            keyboard = types.InlineKeyboardMarkup()
            url_button1 = types.InlineKeyboardButton(text="📝 My data", callback_data='Data')
            keyboard.add(url_button1)
            WELCOME_MESSAGE = f"""
            <b>Thank you {name}!</b>

        Don't forget to:
        🔸️ Stay in the telegram channels
        Your personal number is {iid}.
            """
            bot.send_message(
                call.message.chat.id,
                WELCOME_MESSAGE,
                parse_mode='html',
                disable_web_page_preview=True,
                reply_markup=keyboard,
            )
        else:
            statuss = ['creator', 'administrator', 'member']
            a = bot.get_chat_member(chat_id=CHAT_ID, user_id=call.message.chat.id).status
            if a in statuss:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="❗️Join now❗️", url='https://t.me/joinchat/9mOknjbsndMxOWIy')
                url_button1 = types.InlineKeyboardButton(text="✅ Done", callback_data='product')
                keyboard.add(url_button, url_button1)
                WELCOME_MESSAGE = f"""🔹️Join my FREE Airdrops & signals telegram channel"""
                bot.send_message(
                    call.message.chat.id,
                    WELCOME_MESSAGE,
                    parse_mode='html',
                    disable_web_page_preview=True,
                    reply_markup=keyboard
                    
                )
            else:
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text="❗️Join now❗️", url='https://t.me/joinchat/KZZmGyKBR802MjQy')
                url_button1 = types.InlineKeyboardButton(text="✅ Done", callback_data='Done')
                keyboard.add(url_button, url_button1)
                WELCOME_MESSAGE = f"""🔹️ You didn't join Airdrop announcement channel"""
                bot.send_message(
                    call.message.chat.id,
                    WELCOME_MESSAGE,
                    parse_mode='html',
                    disable_web_page_preview=True,
                    reply_markup=keyboard
                    
                )

CHAT_ID1 = -1001380675893

@bot.callback_query_handler(func=lambda call: call.data.startswith('product'))
def callback_worker_calc(call):
    if call.message.chat.username in dic:
        iid = dic[call.message.chat.username]
        iid = iid['num']
        name = call.message.chat.first_name
        keyboard = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="📝 My data", callback_data='Data')
        keyboard.add(url_button1)
        WELCOME_MESSAGE = f"""
        <b>Thank you {name}!</b>

    Don't forget to:
    🔸️ Stay in the telegram channels
    Your personal number is {iid}.
        """
        bot.send_message(
            call.message.chat.id,
            WELCOME_MESSAGE,
            parse_mode='html',
            disable_web_page_preview=True,
            reply_markup=keyboard,
        )
    else:
        statuss = ['creator', 'administrator', 'member']
        a = bot.get_chat_member(chat_id=CHAT_ID1, user_id=call.message.chat.id).status
        if a in statuss:
            bot.send_message(
                call.message.chat.id,
                'Submit SafeMars Bep20 Address (binance smart chain). You can find this wallet address at Trustwallet.',
            )
            bot.register_next_step_handler(call.message, view_number)
        else:
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="❗️Join now❗️", url='https://t.me/joinchat/9mOknjbsndMxOWIy')
            url_button1 = types.InlineKeyboardButton(text="✅ Done", callback_data='product')
            keyboard.add(url_button, url_button1)
            WELCOME_MESSAGE = f"""🔹️ You didn't join FREE Airdrops & signals channel"""
            bot.send_message(
                call.message.chat.id,
                WELCOME_MESSAGE,
                parse_mode='html',
                disable_web_page_preview=True,
                reply_markup=keyboard                
                )
    
w = 1
def view_number(message):
    global w
    num = message.chat.id
    name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text="📝 My data", callback_data='Data')
    keyboard.add(url_button1)
    WELCOME_MESSAGE = f"""
    <b>Thank you {name}!</b>

Don't forget to:
🔸️ Stay in the telegram channels
Your personal number is {w}.
    """
    bot.send_message(
        message.from_user.id,
        WELCOME_MESSAGE,
        parse_mode='html',
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )
    usern = message.from_user.username
    w = w + 1
    nim = w - 1
    values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": f"A{w}",
             "majorDimension": "ROWS",
             "values": [[usern, message.text, nim]]},
            
        ]
        }
    ).execute()
    dic[message.from_user.username] = {'id': w, 'cash': message.text, 'num': w-1}


@bot.callback_query_handler(func=lambda call: call.data.startswith('Data'))
def callback_wdata_calc(call):
    iid = dic[call.message.chat.username]
    iid = iid['num']
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text="📝 Change wallet", callback_data='Change')
    keyboard.add(url_button1)
    cah = dic[call.message.chat.username]
    WELCOME_MESSAGE = f"""
Your details:
-------------------

Telegram: {call.message.chat.username}
BEP20 wallet: {cah['cash']}
Number: {iid}
    """
    bot.send_message(
        call.message.chat.id,
        WELCOME_MESSAGE,
        parse_mode='html',
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith('Change'))
def callback_wdata_calc(call):
    bot.send_message(
        call.message.chat.id,
        'Submit SafeMars Bep20 Address (binance smart chain). You can find this wallet address at Trustwallet.',
        )
    bot.register_next_step_handler(call.message, change_number)


def change_number(message):
    iid = dic[message.chat.username]
    iid = iid['id']
    num = dic[message.chat.username]
    num = num['num']
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text="📝 My data", callback_data='Data')
    keyboard.add(url_button1)

    usern = message.from_user.username
    values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": f"A{iid}",
             "majorDimension": "ROWS",
             "values": [[usern, message.text, num]]},
            
        ]
        }
    ).execute()
    cah = dic[message.chat.username]
    cah['cash'] = message.text

    bot.send_message(
        message.chat.id,
        'Done',
        parse_mode='html',
        disable_web_page_preview=True,
        reply_markup=keyboard,
        )

        
bot.polling()
