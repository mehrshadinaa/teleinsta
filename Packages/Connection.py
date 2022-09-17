import requests

TOKEN = "5700792783:AAHSmf1EMAiZ6wtIL8-69JceQxPN5TphSiU"
URL = "https://api.telegram.org/bot%s/"%TOKEN

proxies = {
   'http': 'socks5h://127.0.0.1:9050',
   'https': 'socks5h://127.0.0.1:9050'
}

def send_url(url):
    print(url)
    response = requests.get(url, proxies=proxies)
    return response.json()

def json_from_url(url):
    getUpdates = send_url(url)
    return getUpdates

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = json_from_url(url)
    return js

def get_last_update_id(updates): # vase ofsset
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def send_message(chat_id, text, reply_markup=dict()):
    json = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup
    }
    print(json)
    requests.post(URL + "sendMessage", json=json, proxies=proxies)

def send_document(doc, chat_id):
    files = {'document': open("/home/parisa/Documents/bot.py")}
    requests.post(URL + "sendDocument?chat_id={}".format(chat_id), files=files)

def send_image(chat_id):
    files = {'photo': open("/home/parisa/Pictures/Screenshot_2021-09-13_10_33_09.png")}
    requests.post(URL + "sendPhoto?chat_id={}".format(chat_id), files=files)
