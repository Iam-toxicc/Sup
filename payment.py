import aiohttp
from config import LOGGER_ID
from database import update_balance

async def verify_upi(bot, user, utr):

    url = "https://bharatpe-taupe.vercel.app/api/verify"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"utr": utr}) as resp:
            data = await resp.json()

    if data.get("status") == "SUCCESS":
        amount = float(data.get("amount_credited"))
        name = data.get("payer_name")

        update_balance(user.id, amount)

        # 🔥 LOGGER
        await bot.send_message(
            LOGGER_ID,
            f"""🤖 Auto-Deposit Alert

👤 User: {user.first_name}
💰 Amount: ₹{amount}
🆔 UTR: {utr}
🏦 Name: {name}"""
        )

        return True, amount

    return False, 0
