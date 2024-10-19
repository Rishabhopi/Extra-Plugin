from pyrogram import filters

from VIPMUSIC import app


@app.on_message(filters.command(["qr"]))
async def write_text(client, message):
    if len(message.command) < 2:
        await message.reply_text("**Usage**:- `/qr https://t.me/rishu1286`")
        return
    text = " ".join(message.command[1:])
    photo_url = "https://dynamicqrcode.nepcoderdevs.workers.dev/?message=" + text
    await app.send_photo(
        chat_id=message.chat.id, photo=photo_url, caption="🍁Here is your Qr code"
    )


__MODULE__ = "Qʀ-ɢᴇɴ"

__HELP__ = """
Ƭʜɪs ᴍᴏᴅᴜʟᴇ ɢᴇɴᴇʀᴀᴛᴇs Qʀ ᴄᴏᴅᴇs. Usᴇ ᴛʜᴇ /qr ᴄᴏᴍᴍᴀɴᴅ ғᴏʟʟᴏᴡᴇᴅ ʙʏ ᴛʜᴇ ᴛᴇxᴛ ᴏʀ URL ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴇɴᴄᴏᴅᴇ ɪɴᴛᴏ ᴀ Qʀ ᴄᴏᴅᴇ. Fᴏʀ ᴇxᴀᴍᴘʟᴇ, `/qr https://t.me/rishu1286`. Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴛʜᴇɴ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Qʀ ᴄᴏᴅᴇ ғᴏʀ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴᴘᴜᴛ. Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ɪɴᴄʟᴜᴅᴇ ᴛʜᴇ ᴘʀᴏᴛᴏᴄᴏʟ (http:// ᴏʀ https://) ғᴏʀ URLs. Eɴᴊᴏʏ ᴄʀᴇᴀᴛɪɴɢ Qʀ ᴄᴏᴅᴇs ᴡɪᴛʜ ᴇᴀsᴇ!
"""
