import json
from Packages.Commands import *
from Packages.Database import check_user

wait_for_new_username = set()

def check_valid_commands(Command):
    if Command in {"/start","/help"}:
        return True
    else:
        return False

"""message_id =
sender_chat =
forward_from =
forward_from_chat =
forward_from_message_id =
forward_signature =
forward_sender_name
forward_date =
is_automatic_forward =
replay_to_message =
via_bot =
edit_date =
has_protect_content=
media_group_id =
author_signature =
entities =
animation =
audio =
document =
sticker =
video =
video_note =
voice =
caption =
caption_entities =
contact =
dice =
game =
poll =
venue =
location =
new_chat_member =
left_chat_member="""


def decision_making(getUpdates):
    for update in getUpdates["result"]:
        if update.get("message") != None:
            #print(json.dumps(getUpdates, indent=4))
            update = update["message"]
            if "from" in update:
                update1 = update["from"]
                from_id = update1["id"]
                from_is_bot = update1["is_bot"]
                from_first_name = update1["first_name"] if "first_name" in update1 else ""
                from_last_name = update1["last_name"] if "last_name" in update1 else ""
                from_username = update1["username"] if "username" in update1 else ""
                from_language_code = update1["language_code"] if "language_code" in update1 else ""
                if from_is_bot == True:
                    from_can_join_groups = update1[
                    "can_join_groups"] if "can_join_groups" in update1 else ""
                    from_can_read_all_group_messages = update1[
                    "can_read_all_group_messages"
                    ] if "can_read_all_group_messages" in update1 else ""
                    from_supports_inline_queries = update1[
                    "supports_inline_queries"
                    ] if "supports_inline_queries" in update1 else ""

            if "chat" in update:
                update1 = update["chat"]
                chat_id = update1["id"]
                chat_type = update1["first_name"]
                chat_title = update1["first_name"] if "first_name" in update1 else ""
                chat_username = update1["username"] if "username" in update1 else ""
                chat_first_name = update1["first_name"] if "first_name" in update1 else ""
                chat_last_name = update1["last_name"] if "last_name" in update1 else ""

            if "photo" in update:
                photo = list()
                for photo_size in update["photo"]:
                    photo.append(
                    [photo_size["file_id"], #file_id
                    photo_size["file_unique_id"], #unique_id
                    photo_size["width"], #width
                    photo_size["height"], #height
                    photo_size["file_size"] if "file_size" in photo_size else 0 #height
                    ])
                #print(photo)

            date = update["date"] if "date" in update else ""
            text = update["text"] if "text" in update else ""

            if chat_id in wait_for_new_username:
                print('im here')
                if text == 'Back🚶🏻‍♂️':
                    wait_for_new_username.remove(chat_id)
                    home(chat_id)
                elif text.startswith('@'):
                    print('im heree')
                    find_username(chat_id, text[1:])


            else:
                match text:
                    case '/start':
                        if check_user(chat_id,from_first_name,
                                        from_last_name,from_username):
                            start(chat_id)
                        else:
                            start_new_user(chat_id)
                    case '/new_person' | 'new_person👫':
                        wait_for_new_username.add(chat_id)
                        new_person(chat_id)
                    case '/my_clients' | 'my_clients📑': #'whats_changed_with_this_id':
                        my_clients(chat_id)
                    case '/my_accounts' | 'my_accounts👔': #'whats_changed_with_this_id':
                        my_accounts(chat_id)
                    case '/home' | 'home🏠': #'whats_changed_with_this_id':
                        home(chat_id)
                    case '/help' | 'help⛑':
                        help(chat_id)
                    case '/Donate' | 'Donate 🤓': #'whats_changed_with_this_id':
                        donate(chat_id)
                    case _ :
                        unknow(chat_id)


        # if there were a post channell do noting
        elif update.get("edited_message") != None:
            pass
        elif update.get("channel_post") != None:
            pass
        elif update.get("edit_channel_post") != None:
            pass
        elif update.get("edited_channel_post") != None:
            pass
        elif update.get("channel_post") != None:
            pass
        elif update.get("inline_query") != None:
            pass
        elif update.get("chosen_inline_result") != None:
            pass
        elif update.get("callback_query") != None:
            try: text = update["message"]["text"]
            except: None

            callback_query_id = getUpdates["result"][i]["callback_query"]['id']
            chat_id = getUpdates["result"][i]["callback_query"]["from"]["id"]
            callback_data = getUpdates["result"][i]["callback_query"]['data']
            message_id = getUpdates["result"][i]["callback_query"]["message"]["message_id"]

        elif update.get("shipping_query") != None:
            pass
        elif update.get("pre_checkout_query") != None:
            pass
        elif update.get("poll") != None:
            pass
        elif update.get("poll_answer") != None:
            pass
        elif update.get("my_chat_member") != None:
            chat_id = str(getUpdates["result"][i]["my_chat_member"]["chat"]["id"])
            title = getUpdates["result"][i]["my_chat_member"]["chat"]["title"]
            username = "Channel type was private"
            try:
                username = getUpdates["result"][i]["my_chat_member"]["chat"]["username"]
            except: None

            # we get our channel information
            #we notice to chairman
            if getUpdates["result"][i]["my_chat_member"]["new_chat_member"]["status"] == "administrator":
                if getUpdates["result"][i]["my_chat_member"]["from"]["id"] == chairman_id:
                    text = "🧰 ربات \(\( seldan🗼\)\) توسط مدیر عضو کانال زیر شد:%0A%0A🧰 نام کانال تلگرام: *{}*%0A🧰آیدی کانال تلگرام: *__{}__*%0A🧰 یوزرنیم کانال تلگرام: *@{}*".format(title,chat_id[1:],username)
                    url = URL + "sendMessage?chat_id=%i&text=%s"%(chairman_id, text) + "&parse_mode=MarkdownV2"
                    send_url(url)
                    introduce_channel(getUpdates["result"][i], username)
                    text1 = read_database(5, username)
                    url = URL + "sendMessage?chat_id=%i&text=%s"%(chairman_id, text1) + "&parse_mode=MarkdownV2"
                    send_url(url)

                # we left from wrong channel
                else:
                    url = URL + "leaveChat?chat_id=%s"%(chat_id)
                    send_url(url)
                    text = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️%0A📣 ربات عضو کانال \(\(*@{}*\)\) شد‼️%0A📣 ربات فقط باید توسط مدیر عضو یک کانال شود‼️%0A〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️".format(username)
                    url = URL + "sendMessage?chat_id=%i&text=%s"%(chairman_id, text) + "&parse_mode=MarkdownV2"
                    send_url(url)

            elif getUpdates["result"][i]["my_chat_member"]["new_chat_member"]["status"] in {"kicked", "left"}:
                text = "📣 ربات از کانال \(\( *@{}* \)\) حذف شد‼️".format(username)
                url = URL + "sendMessage?chat_id=%i&text=%s"%(chairman_id, text) + "&parse_mode=MarkdownV2"
                send_url(url)
                delete_from_database(1,title)

        elif update.get("chat_join_requests") != None:
            pass
