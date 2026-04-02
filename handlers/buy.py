from hydrogram import Client, filters
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query(filters.regex("buy"))
async def buy_menu(c, cb):
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇮🇳 UPI", callback_data="upi"),
            InlineKeyboardButton("🪙 Crypto", callback_data="crypto")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="home")
        ]
    ])

    await cb.message.edit_text(
        "💳 Choose Payment Method",
        reply_markup=buttons
    )
