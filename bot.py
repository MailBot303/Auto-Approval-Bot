from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://telegra.ph/file/4d384e0ad29af76974c4c.jpg',
    'https://telegra.ph/file/4d384e0ad29af76974c4c.jpg',
    'https://telegra.ph/file/4d384e0ad29af76974c4c.jpg'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_photo(kk.id,img, "**⚡️ 1080 GB Collection ⚡️\nc#p/r#p/mom+son/desi/mallu\n\nAll Category Videos Available\n\nClick Here To Download ✔️\n👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻\n\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔞+ Group ", url="https://t.me/Chatting_Group_Adult"),
                        InlineKeyboardButton("🗂 Repo", url="https://pastebin.com/raw/sK5NzESH")
                    ],[
                        InlineKeyboardButton("📞 Call Me +91765586....", url="https://cutt.ly/dwlJZqqM")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/8d3d89c94a6952bf835ef.jpg", caption="**🥰 Hello {}!\nI'm your s*xy partner 💋💋\nI can help you cum 💦\n\nWatch me taking bath\n👇👇\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me in private 💁‍♂️", url="https://t.me/vjmasterblastbot?startgroup")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🤖 Hello {}!\nwrite me in private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Join 🔞+ Group", url="https://t.me/Chatting_Group_Adult")
                ]
            ]
        )
        await m.reply_text("**🥵 Watch My Hot N*de Videos 💦\nClick here👇👇\n\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM\n\nPlease Join https://t.me/+FkBARZVToxRmNzc1 to use me.\nIf you already joined click /start to continue.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#@app.on_callback_query(filters.regex("chk"))
#async def chk(_, cb : CallbackQuery):
   # try:
      #  await app.get_chat_member(cfg.CHID, cb.from_user.id)
       # if cb.message.chat.type == enums.ChatType.PRIVATE:
        #    keyboard = InlineKeyboardMarkup(
         #       [
            #        [
            #            InlineKeyboardButton("🔞+ Group ", url="https://t.me/Chatting_Group_Adult"),
           #             InlineKeyboardButton("🗂 Repo", url="https://pastebin.com/raw/sK5NzESH")
           #         ],[
            #            InlineKeyboardButton("📞 Call Me +91765586....", url="https://cutt.ly/dwlJZqqM")
           #         ]
         #       ]
  #          )
 #           add_user(cb.from_user.id)
#            await cb.message.edit("**🥰 Hello {}!\nI'm your s*xy partner 💋💋\nI can help you cum 💦\n\nWatch me taking bath\n👇👇\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM\nhttps://cutt.ly/dwlJZqqM __**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
 #       print(cb.from_user.first_name +" Is started Your Bot!")
 #   except UserNotParticipant:
 #       await cb.answer("🙅‍♂️ You did not joined the channel, Join and try again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    if m.reply_to_message is None:
        await m.reply_text("Please reply to a message to broadcast.")
        return

    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅ Successful to `{success}` users.\n❌ Failed to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
