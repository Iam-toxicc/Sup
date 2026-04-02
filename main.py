from hydrogram import Client, filters
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, ADMINS
from database import add_user
from payment import verify_upi

bot = Client("storebot", bot_token=BOT_TOKEN)

# 🚀 START
@bot.on_message(filters.command("start"))
async def start(c, m):
    add_user(m.from_user.id, m.from_user.first_name)

    text = """🔥 Interfaith Media Store

Choose option 👇"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("📦 Plans", callback_data="plans")],
        [InlineKeyboardButton("💳 Buy", callback_data="buy")]
    ])

    await m.reply_text(text, reply_markup=buttons)

# 💳 BUY MENU
@bot.on_callback_query(filters.regex("buy"))
async def buy(c, cb):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🇮🇳 UPI", callback_data="upi")],
        [InlineKeyboardButton("🔙 Back", callback_data="home")]
    ])
    await cb.message.edit_text("💳 Payment", reply_markup=buttons)

# 🇮🇳 UPI START
@bot.on_callback_query(filters.regex("upi"))
async def upi(c, cb):
    await cb.message.edit_text(
        "Send UTR after payment to verify"
    )

# 🧠 UTR INPUT
@bot.on_message(filters.text & filters.private)
async def handle_utr(c, m):
    utr = m.text.strip()

    if len(utr) == 12 and utr.isdigit():
        ok, amount = await verify_upi(c, m.from_user, utr)

        if ok:
            await m.reply_text(f"✅ Payment Success ₹{amount}")
        else:
            await m.reply_text("❌ Verification failed")

bot.run()
