import asyncio
from telethon import TelegramClient, events

# ⚠️ Nhập API ID và HASH tại đây
api_id = 16150243
api_hash = 'd49c0c3277105edb4b944b03c23311c8'
session_name = 'session'  # file lưu phiên đăng nhập

# Nội dung auto-reply
auto_reply_text = (
    "🌟 **[Vui Lòng Đợi Admin Hiện Tại Đang Offline Hoặc Đang Nhận Nhiều Tin Nhắn]**\n"
    "🟢 **[Bạn Nên]**\n"
    "☑️ Vô Thẳng Vấn Đề Cần Hỏi !\n"
    "☑️ Không Lòng Vòng\n"
    "☑️ Thời Gian Hoạt Động [9:00pm-12:00am]\n"
    "🇻🇳 **[Chúc Bạn Nói Chuyện Với Admin Vui Vẻ]**\n"
    "\nTin Nhắn Từ Bot !"
)

# Danh sách user đã được trả lời
replied_users = set()

# Tạo client Telethon
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    sender_id = sender.id
    chat = await event.get_chat()
    
    # Không phản hồi tin nhắn nhóm
    if event.is_group or event.is_channel:
        return

    me = await client.get_me()
    if sender_id == me.id:
        return

    if sender_id in replied_users:
        return

    await event.respond(auto_reply_text, parse_mode='markdown')
    replied_users.add(sender_id)
    print(f"Đã trả lời tự động cho user: {sender_id}")

async def main():
    await client.start()
    print("🤖 Bot đang hoạt động...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
