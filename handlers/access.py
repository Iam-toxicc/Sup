from hydrogram import Client
from config import CHANNELS

async def give_access(c, user_id, category):

    channel_id = CHANNELS.get(category)

    if not channel_id:
        return

    try:
        await c.add_chat_members(channel_id, user_id)
    except Exception as e:
        print("Access Error:", e)
