from os.path import abspath, exists
import sqlite3 as sl

database_location1 = abspath(__file__)
database_location = database_location1[:-20] + "/database.sqlite3"


def check_database():
    #print(os.path.abspath(database_lacation))
    return exists(database_location)

def create_database():
    con = sl.connect(str(database_location))
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE bot_users (
    chat_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    username TEXT
        );
    """)
    con.commit()
    con.close()

def create_table(username):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE \"{}\" (
    username TEXT,
    folower INTEGER,
    folowing INTEGER
        );
    '''.format(username))
    con.commit()
    con.close()

def check_table(username):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    for table in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        if table[0] == username:
            return True #hast
    else:
        return False #nist
    con.close()

def check_user(chat_id,first_name="",last_name="",username=""):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    if read_database(1, chat_id) == False: #new_user
        write_in_database('users',[chat_id,first_name,last_name,username])
        return False
    else: #old_user
        return True
    con.close()

def write_in_database(table, data, folower=0, folowing=0):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    if table == 'users':
        query = (
            'INSERT INTO \"bot_users\" (chat_id, first_name, last_name, username) '
            'VALUES ({},\"{}\",\"{}\",\"{}\")'.format(data[0], data[1], data[2],data[3])
        )
    else:
        query = (
            'INSERT INTO \"{}\" (username, folower, folowing) '
            'VALUES (\"{}\",{},{})'.format(table, data, folower, folowing)
        )
    cur.execute(query)
    con.commit()
    con.close()

def update_database():
    con = sl.connect(str(database_location))
    cur = con.cursor()
    """
    if key == "first_name":
        query = "UPDATE \"bot_users\" SET \"first_name\" = \"{}\" WHERE chat_id = {}".format(key2, chat_id)
    elif key == "sex":
        query = "UPDATE \"bot_users\" SET sex = \"{}\" WHERE chat_id = {}".format(key2, chat_id)
    #print("\n\n", query, "\n\n")
    """
    cur.execute(query)
    con.commit()
    con.close()

def read_database(number,id_person,chat_id=None):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    #print("we are connected to database telegram")
    if number == 1:
        query = "SELECT chat_id FROM \"bot_users\""
        for chat_id in cur.execute(query):
            if id_person in chat_id:
                return True #hast
        return False

    elif number == 2:
        first_name=None
        query = "SELECT first_name from \"bot_users\" WHERE chat_id = {}".format(id_person)
        for x in cur.execute(query):
            first_name = x[0]
        return first_name
    con.close()

def delete_from_database(number, id_person):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    if number == 1:
        query = "DELETE from channels WHERE \"title_c\" = \"{}\"".format(id_person)
    #print("\n\n", query, "\n\n")
    cur.execute(query)
    con.commit()
    con.close()

def write_channel(json, username):
    con = sl.connect(str(database_location))
    cur = con.cursor()
    chat_id_c = json["my_chat_member"]["chat"]["id"]
    title_c = json["my_chat_member"]["chat"]["title"]
    username_c = username
    print(username_c)
    status = json["my_chat_member"]["new_chat_member"]["status"]
    can_be_edited = json["my_chat_member"]["new_chat_member"]["can_be_edited"]
    can_manage_chat = json["my_chat_member"]["new_chat_member"]["can_manage_chat"]
    can_change_info = json["my_chat_member"]["new_chat_member"]["can_change_info"]
    can_post_messages = json["my_chat_member"]["new_chat_member"]["can_post_messages"]
    can_edit_messages = json["my_chat_member"]["new_chat_member"]["can_edit_messages"]
    can_delete_messages = json["my_chat_member"]["new_chat_member"]["can_delete_messages"]
    can_invite_users = json["my_chat_member"]["new_chat_member"]["can_invite_users"]
    can_restrict_members = json["my_chat_member"]["new_chat_member"]["can_restrict_members"]
    can_promote_members = json["my_chat_member"]["new_chat_member"]["can_promote_members"]
    can_manage_voice_chats = json["my_chat_member"]["new_chat_member"]["can_manage_voice_chats"]
    is_anonymous = json["my_chat_member"]["new_chat_member"]["is_anonymous"]

    query = """INSERT INTO channels (
            chat_id_c,
            title_c,
            username_c ,
            status ,
            can_be_edited ,
            can_manage_chat ,
            can_change_info ,
            can_post_messages ,
            can_edit_messages ,
            can_delete_messages ,
            can_invite_users ,
            can_restrict_members ,
            can_promote_members ,
            can_manage_voice_chats ,
            is_anonymous
            )
            VALUES
            (\"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\"
            )""".format(chat_id_c,title_c,username_c,status,can_be_edited,can_manage_chat,can_change_info,can_post_messages,can_edit_messages,can_delete_messages,can_invite_users,can_restrict_members,can_promote_members,can_manage_voice_chats,is_anonymous)
    #print("\n\n", query, "\n\n")
    cur.execute(query)
    con.commit()
    con.close()
