import logging
import logging.config

# Load logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.WARNING)

import asyncio
from pyrogram import Client

# ⚠️ Hardcode your API credentials here:
API_ID = 19976712          # replace with your actual API ID (integer)
API_HASH = "1f883776601877c632d76d845fffe74d"  # replace with your actual API hash (string)

async def main():
    """Generate session string for user bot"""

    phone_number = input('Enter phone number with country code prefix: ')

    user_bot = Client(
        name='User-bot',
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=phone_number,
        in_memory=True  # Session won't be saved to disk
    )

    async with user_bot:
        session_string = await user_bot.export_session_string()
        print("\n🔑 Your session string:\n")
        print(session_string)

if __name__ == '__main__':
    asyncio.run(main())
