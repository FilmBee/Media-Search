## 🔔 Follow Us Here For More

### [YouTube Channel](https://youtube.com/@TechnoFoxYT)

### [Telegram Group](https://t.me/webcoderhub)

### [Blog Site](https://webcoderhub.blogspot.com)

 ## Give Me A Star ⭐ 
>After 50+ stars on this Project I will Release a New Modified Version Of This Bot With IMDb Support & more.

# [Media Search bot](https://github.com/ScripterSaurav/telegram-movie-search-bot)

* Index channel or group files for inline search.
* When you post file on telegram channel or group this bot will save that file in database, so you can search easily in inline mode.
* Supports document, video and audio file formats with caption support.

### Easy Way
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Hard Way
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
env\Scripts\activate.bat # For Windows
source env/bin/activate # For Linux or MacOS

# Install Packages
pip3 install -r requirements.txt

# Edit info.py with variables as given below then run bot
python3 bot.py
```
Check [`sample_info.py`](sample_info.py) before editing [`info.py`](info.py) file

### Docker
```
docker run -d \
    -e BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" \
    -e API_ID='12345' \
    -e API_HASH='0123456789abcdef0123456789abcdef' \
    -e CHANNELS='-10012345678' \
    -e ADMINS='123456789' \
    -e DATABASE_URI="mongodb+srv://...mongodb.net/Database?retryWrites=true&w=majority" \
    -e DATABASE_NAME=databasename \
    --restart on-failure \
    --name mediasearchbot botxtg/media-search-bot
```
You can also run with `env` file like below,
```
docker run -d \ 
     --env-file .env \
     --restart on-failure \
     --name mediasearchbot botxtg/media-search-bot
```

## Variables
### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space

* `DATABASE_URI_MOVIE`: MongoDB URI for movie files database.
* `DATABASE_NAME_MOVIE`: Database name for movie files.
* `COLLECTION_NAME_MOVIE`: Collection name for movie files.

* `DATABASE_URI_SERIES`: MongoDB URI for series files database.
* `DATABASE_NAME_SERIES`: Database name for series files.
* `COLLECTION_NAME_SERIES`: Collection name for series files.

* `USERDATA_DB_URI`: MongoDB URI for user/referral/admin data.
* `USERDATA_DB_NAME`: Database name for user/referral/admin data.
* `USERDATA_COLLECTION`: Collection name for user/referral/admin data.

### Optional Variables
* `CACHE_TIME`: The maximum amount of time in seconds that the result of the inline query may be cached on the server
* `USE_CAPTION_FILTER`: Whether bot should use captions to improve search results. (True/False)
* `AUTH_USERS`: Username or ID of users to give access of inline search. Separate multiple users by space. Leave it empty if you don't want to restrict bot usage.
* `AUTH_CHANNEL`: Username or ID of channel. Without subscribing this channel users cannot use bot.
* `START_MSG`: Welcome message for start command.
* `INVITE_MSG`: Auth channel invitation message.
* `USERBOT_STRING_SESSION`: User bot string session.
* `ENABLE_REFERRAL`: Enable referral system (True/False).
* `REQUIRED_REFERRALS`: Number of successful referrals required to unlock bot.
* `MOVIE_CHANNEL_ID`: Channel/group ID for movies (use -100... format).
* `SERIES_CHANNEL_ID`: Channel/group ID for series (use -100... format).

## Admin commands
```
channel - Get basic infomation about channels
total - Show total of saved files
delete - Delete file from database
index - Index all files from channel or group
logger - Get log file
```

## Tips
* Use `index` command or run [one_time_indexer.py](one_time_indexer.py) file to save old files in the database that are not indexed yet.
* You can use `|` to separate query and file type while searching for specific type of file. For example: `Avengers | video`
* If you don't want to create a channel or group, use your chat ID / username as the channel ID. When you send a file to a bot, it will be saved in the database.

## Contributions
Contributions are welcome.

## Thanks to [Pyrogram](https://github.com/pyrogram/pyrogram)

## Support
[Update Channel](https://t.me/TechnofoxYT) and [Support Group](https://t.me/webcoderhub)

## License
Code released under [The GNU General Public License](LICENSE).

