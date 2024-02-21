from Rudra import *
from Rudra import Rudra1, Rudra2, Rudra3, Rudra4, Rudra5
from telethon import events

a = False

@Rudra1.on(events.NewMessage(incoming=True, pattern='/spam'))
@Rudra2.on(events.NewMessage(incoming=True, pattern='/spam'))
@Rudra3.on(events.NewMessage(incoming=True, pattern='/spam'))
@Rudra4.on(events.NewMessage(incoming=True, pattern='/spam'))
@Rudra5.on(events.NewMessage(incoming=True, pattern='/spam'))
async def spam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[6:8])
            spam = text[8:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                    await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@Rudra1.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Rudra2.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Rudra3.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Rudra4.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@Rudra5.on(events.NewMessage(incoming=True, pattern='/bigspam'))
async def bigspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[9:15])
            spam = text[15:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                            await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@Rudra1.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Rudra2.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Rudra3.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Rudra4.on(events.NewMessage(incoming=True, pattern='/mspam'))
@Rudra5.on(events.NewMessage(incoming=True, pattern='/mspam'))
async def mspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[7:13])
            if e.is_reply == False:
                await e.client.send_message(e.chat_id, "Please reply to a media and enter how many times you want send that media!")
            elif e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.media
                for i in range(counts):
                    await e.client.send_file(e.chat_id, replied_message)
            else:
                await e.client.send_message(e.chat_id, "Some thing went wrong! Please reply to a media and enter how many times you want send that media!")
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Please enter how many times you want to spam in reply of media!")

@Rudra1.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Rudra2.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Rudra3.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Rudra4.on(events.NewMessage(incoming=True, pattern="/uspam"))
@Rudra5.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        
@Rudra1.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Rudra2.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Rudra3.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Rudra4.on(events.NewMessage(incoming=True, pattern="/ustop"))
@Rudra5.on(events.NewMessage(incoming=True, pattern="/ustop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "U Spam Stopped Successfully")
