from Rudra import *
from Rudra import Rudra1, Rudra2, Rudra3, Rudra4, Rudra5
from telethon import events, Button


data  = [
    Button.url("Channel", url="t.me/RUDRA_JAAT_BIO"),
    Button.url("Repo", url="https://github.com/RUDRA-JAAT/Rudra-Spam"),
    Button.url("Owner", url="https://t.me/Harry8262")
]


@Rudra1.on(events.NewMessage(incoming=True, pattern='/start'))
@Rudra2.on(events.NewMessage(incoming=True, pattern='/start'))
@Rudra3.on(events.NewMessage(incoming=True, pattern='/start'))
@Rudra4.on(events.NewMessage(incoming=True, pattern='/start'))
@Rudra5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[RUDRA-JAAT](tg://user?id={6783196044})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hey {mention},
    This is Rudra Spam Bot.
    A Powerfull Spam Bot With a
    large abusive database.
    So,enjoy the Game!!😈😈
***---------------------------------------***
Owner:- {myOwner}
***---------------------------------------***
Sudo:- {sudo_user}
***---------------------------------------***
Creator:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
