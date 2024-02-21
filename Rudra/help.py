from Rudra import *
from Rudra import Rudra1, Rudra2, Rudra3, Rudra4, Rudra5
from Rudra.helpers.commands import *
from telethon import events, Button

DISPLAY_PICS = "https://telegra.ph/file/c5bca470a1a4596df56f3.jpg"

Buttons = [
    Button.inline("𝗔𝗟𝗜𝗩𝗘", b'alive'),
    Button.inline("𝗣𝗜𝗡𝗚", b'ping')
], [
    Button.inline("𝗥𝗔𝗜𝗗", b'raid'),
    Button.inline("𝗥𝗘𝗣𝗟𝗬 𝗥𝗔𝗜𝗗", b'replyraid')
], [
    Button.inline("𝗦𝗣𝗔𝗠", b'spam'),
    Button.inline("𝗣𝗦𝗣𝗔𝗠", b'pspam')
], [
    Button.inline("𝐄𝐗𝐓𝐑𝐀𝐒", b'extras')
], [
    Button.url("𝐂𝐇𝐀𝐍𝐍𝐄𝐋", "t.me/RUDRA_JAAT_BIO"),
    Button.url("𝐆𝐑𝐎𝐔𝐏", "t.me/HINATA_CHATTING")
]

BACK = [
    Button.inline("Back", b'back')
]

@Rudra1.on(events.NewMessage(incoming=True, pattern='/help'))
@Rudra2.on(events.NewMessage(incoming=True, pattern='/help'))
@Rudra3.on(events.NewMessage(incoming=True, pattern='/help'))
@Rudra4.on(events.NewMessage(incoming=True, pattern='/help'))
@Rudra5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PICS, caption="𝐇𝐄𝐘!! 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐑𝐔𝐃𝐑𝐀 𝐒𝐏𝐀𝐌𝐁𝐎𝐓. 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐘𝐎 𝐔𝐑 𝐇𝐄𝐋𝐏 𝐂𝐎𝐌𝐌𝐀𝐍𝐃!!!", buttons=Buttons)

        

