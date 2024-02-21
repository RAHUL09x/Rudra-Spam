from Rudra import *
from Rudra import Rudra1, Rudra2, Rudra3, Rudra4, Rudra5
from telethon import events
from datetime import datetime

PING_PIC = "https://telegra.ph/file/c5bca470a1a4596df56f3.jpg"

@Rudra1.on(events.NewMessage(incoming=True, pattern='/ping'))
@Rudra2.on(events.NewMessage(incoming=True, pattern='/ping'))
@Rudra3.on(events.NewMessage(incoming=True, pattern='/ping'))
@Rudra4.on(events.NewMessage(incoming=True, pattern='/ping'))
@Rudra5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f" {PING_PIC}\n𝐏𝐈𝐍𝐆 𝐏𝐎𝐍𝐆!!!\n***--------------***\n𝐑𝐔𝐃𝐑𝐀 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓\n***--------------***\n𝒎𝒚 𝒎𝒂𝒔𝒕𝒆𝒓:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n***--------------***\n𝐏𝐈𝐍𝐆!!:- {ms} ms\n***--------------***\n𝐑𝐔𝐃𝐑𝐀 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓 𝐎𝐍 𝐅𝐈𝐑𝐄༗.")
