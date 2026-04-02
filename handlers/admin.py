from hydrogram import Client, filters
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS
from database import users

def is_admin(user_id):
    return user_id in ADMINS

# 👑 ADMIN PANEL
@Client.on_message(filters.command("admin"))
async def admin_panel(c, m):
    if not is_admin(m.from_user.id):
        return

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats"),
            InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")
        ]
    ])

    await m.reply_text("👑 Admin Panel", reply_markup=buttons)

# 📊 STATS
@Client.on_callback_query(filters.regex("stats"))
async def stats(c, cb):
    total = users.count_documents({})
    await cb.message.reply_text(f"📊 Total Users: {total}")
