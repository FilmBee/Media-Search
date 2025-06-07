import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.WARNING)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from pyrogram.types import Message
from utils import add_user, check_and_activate, get_user, get_total_counts
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, ENABLE_REFERRAL, REQUIRED_REFERRALS


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

        @self.on_message(filters.command("start") & filters.private)
        async def start_cmd(client, message: Message):
            args = message.text.split()
            user_id = message.from_user.id
            referrer = None
            if len(args) > 1:
                referrer = int(args[1]) if args[1].isdigit() else None
            await add_user(user_id, referrer)
            if ENABLE_REFERRAL:
                user = await get_user(user_id)
                if not user.get('active', False):
                    await check_and_activate(user_id)
                    user = await get_user(user_id)
                    if not user.get('active', False):
                        needed = REQUIRED_REFERRALS - user.get('ref_count', 0)
                        link = f"https://t.me/{self.username[1:]}?start={user_id}"
                        await message.reply(
                            f"👋 Welcome!\n\n"
                            f"To unlock the bot, invite {needed} more user(s) using your referral link:\n\n"
                            f"`{link}`\n\n"
                            f"Your referrals: {user.get('ref_count', 0)}/{REQUIRED_REFERRALS}"
                        )
                        return
            await message.reply(
                "✅ Welcome! You can now use the bot.\n"
                "Use inline mode to search files, or /total to see file stats."
            )

        @self.on_message(filters.command("total") & filters.private)
        async def total_cmd(client, message: Message):
            movie_count, series_count, total = await get_total_counts()
            await message.reply(
                f"📊 **File Stats**\n"
                f"Movies: `{movie_count}`\n"
                f"Series: `{series_count}`\n"
                f"Total: `{total}`"
            )

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = Bot()
app.run()
