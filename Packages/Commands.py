from Packages.Connection import send_message
from Packages.Instagram import find_profile

def new_person(chat_id):
    text = 'Hey just send your target instagram username:'
    reply_markup = {
        'keyboard': [
            ['Back🚶🏻‍♂️']
        ],
        "resize_keyboard": True
    }
    send_message(chat_id, text, reply_markup)

def find_username(chat_id, username):
    text = 'Im searching for user! 🔍'
    send_message(chat_id, text)
    profile, folowers, folowing = find_profile(username)
    send_message(chat_id, profile)
    send_message(chat_id, folowers)
    send_message(chat_id, folowing)

def my_clients(chat_id):
    pass

def my_accounts(chat_id):
    pass

def home(chat_id):
    text = 'You are at /home page\n choose an option👇🏻'
    reply_markup = {
        'keyboard': [
            ['new_person👫','my_clients📑'],
            ['my_accounts👔','home🏠','help⛑'],
            ['Donate 🤓']
        ],
        "resize_keyboard": True
    }
    send_message(chat_id, text, reply_markup)

def help(chat_id):
    text = "You have send /help command"
    send_message(chat_id, text)

def donate(chat_id):
    text = "I will explain you"
    send_message(chat_id, text)

def start_new_user(chat_id):
    text = (
        "Hi, you are new to me.\n"
        "you didn't used this bot before!\n"
        "i can do so many tasks🥹\n"
        "i can kill anyone you want!"
    )
    reply_markup = {
        'keyboard': [
            ['new_person👫','my_clients📑'],
            ['my_accounts👔','home🏠','help⛑'],
            ['Donate 🤓']
        ],
        "resize_keyboard": True
    }
    send_message(chat_id, text, reply_markup)

def start(chat_id):
    text = (
        "hi :)\n"
        "i can do so many tasks🥹\n"
        "i can kill anyone you want!"
    )
    reply_markup = {
        'keyboard': [
            ['new_person👫','my_clients📑'],
            ['my_accounts👔','home🏠','help⛑'],
            ['Donate!']
        ],
        "resize_keyboard": True
    }
    send_message(chat_id, text, reply_markup)

def unknow(chat_id):
    text = "I don't undresstand what you said!\nuse the keys"
    reply_markup = {
        'keyboard': [
            ['new_person👫','my_clients📑'],
            ['my_accounts👔','home🏠','help⛑'],
            ['Donate 🤓']
        ],
        "resize_keyboard": True
    }
    send_message(chat_id, text, reply_markup)
