from Packages.Database import create_table, check_table, write_in_database
import instaloader

loader = instaloader.Instaloader()

# login
try:
    loader.load_session_from_file('mehrshadina')
except FileNotFoundError:
    loader.context.log("Session file does not exist yet - Logging in.")
if not loader.context.is_logged_in:
    loader.login('mehrshadina', 'newlifebegin')
    loader.save_session_to_file()


def find_profile(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
    except ProfileNotExistsException:
        return 'User not find'

    if check_table(username) == False:
        create_table(username)
    else:
        pass

    text = (
        f'🆔 Account:  @{username}\n'
        '=========================================\n'
        f'📇 bio:\n{profile.biography}\n'
        f'🗃 followers: {profile.followers}\n'
        f'🗃 folowings: {profile.followees}'
    )
    text1 = '🗃 followers:\n\n'
    text2 = '🗃 followings:\n\n'

    write_in_database(
        username,
        'bio:{} followers:{} folowings:{}'.format(
            profile.biography,
            profile.followers,
            profile.followees
        )
    )
    for follower in profile.get_followers():
        text1 += follower.username + '\n'
        write_in_database(
            username,
            follower.username,
            folower=1
        )
    for following in profile.get_followees():
        text2 += following.username + '\n'
        write_in_database(
            username,
            following.username,
            folowing=1
        )

    return text, text1, text2
