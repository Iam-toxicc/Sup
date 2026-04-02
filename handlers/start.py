from hydrogram import Client, filters
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user
from config import LOGGER_ID

@Client.on_message(filters.command("start"))
async def start_handler(c, m):
    add_user(m.from_user.id, m.from_user.first_name)

    # 🔥 LOGGER
    await c.send_message(
        LOGGER_ID,
        f"""🚀 New User Started

👤 Name: {m.from_user.first_name}
🆔 ID: {m.from_user.id}
📛 Username: @{m.from_user.username if m.from_user.username else 'No Username'}"""
    )

    text = """🔥 Interfaith Media Store

💎 Premium & Trusted  
⚡ Instant Access  

👇 Choose option"""

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📦 Plans", callback_data="plans"),
