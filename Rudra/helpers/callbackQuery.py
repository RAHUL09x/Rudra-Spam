from Rudra import *
from Rudra import Rudra1, Rudra2, Rudra3, Rudra4, Rudra5
from Rudra.help import *
from Rudra.helpers.commands import *
from telethon import events


@Rudra1.on(events.CallbackQuery(data=b'alive'))
@Rudra2.on(events.CallbackQuery(data=b'alive'))
@Rudra3.on(events.CallbackQuery(data=b'alive'))
@Rudra4.on(events.CallbackQuery(data=b'alive'))
@Rudra5.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'ping'))
@Rudra2.on(events.CallbackQuery(data=b'ping'))
@Rudra3.on(events.CallbackQuery(data=b'ping'))
@Rudra4.on(events.CallbackQuery(data=b'ping'))
@Rudra5.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'raid'))
@Rudra2.on(events.CallbackQuery(data=b'raid'))
@Rudra3.on(events.CallbackQuery(data=b'raid'))
@Rudra4.on(events.CallbackQuery(data=b'raid'))
@Rudra5.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'replyraid'))
@Rudra2.on(events.CallbackQuery(data=b'replyraid'))
@Rudra3.on(events.CallbackQuery(data=b'replyraid'))
@Rudra4.on(events.CallbackQuery(data=b'replyraid'))
@Rudra5.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'spam'))
@Rudra2.on(events.CallbackQuery(data=b'spam'))
@Rudra3.on(events.CallbackQuery(data=b'spam'))
@Rudra4.on(events.CallbackQuery(data=b'spam'))
@Rudra5.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'pspam'))
@Rudra2.on(events.CallbackQuery(data=b'pspam'))
@Rudra3.on(events.CallbackQuery(data=b'pspam'))
@Rudra4.on(events.CallbackQuery(data=b'pspam'))
@Rudra5.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'extras'))
@Rudra2.on(events.CallbackQuery(data=b'extras'))
@Rudra3.on(events.CallbackQuery(data=b'extras'))
@Rudra4.on(events.CallbackQuery(data=b'extras'))
@Rudra5.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@Rudra1.on(events.CallbackQuery(data=b'back'))
@Rudra2.on(events.CallbackQuery(data=b'back'))
@Rudra3.on(events.CallbackQuery(data=b'back'))
@Rudra4.on(events.CallbackQuery(data=b'back'))
@Rudra5.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 