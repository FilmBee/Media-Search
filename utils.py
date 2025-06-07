import motor.motor_asyncio
from types import SimpleNamespace
from info import (
    DATABASE_URI_MOVIE, DATABASE_NAME_MOVIE, COLLECTION_NAME_MOVIE,
    DATABASE_URI_SERIES, DATABASE_NAME_SERIES, COLLECTION_NAME_SERIES,
    USERDATA_DB_URI, USERDATA_DB_NAME, USERDATA_COLLECTION,
    ENABLE_REFERRAL, REQUIRED_REFERRALS,
    MOVIE_CHANNEL_ID, SERIES_CHANNEL_ID
)

# DB clients
movie_client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI_MOVIE)
series_client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI_SERIES)
userdata_client = motor.motor_asyncio.AsyncIOMotorClient(USERDATA_DB_URI)

movie_db = movie_client[DATABASE_NAME_MOVIE][COLLECTION_NAME_MOVIE]
series_db = series_client[DATABASE_NAME_SERIES][COLLECTION_NAME_SERIES]
user_db = userdata_client[USERDATA_DB_NAME][USERDATA_COLLECTION]

async def save_file(media, channel_id=None):
    """Save file to the appropriate db based on channel_id."""
    if channel_id == MOVIE_CHANNEL_ID:
        db = movie_db
    elif channel_id == SERIES_CHANNEL_ID:
        db = series_db
    else:
        db = movie_db  # fallback
    doc = media.__dict__ if hasattr(media, '__dict__') else dict(media)
    await db.update_one(
        {'file_id': doc['file_id']},
        {'$set': doc},
        upsert=True
    )

async def get_search_results(query, file_type=None, max_results=10, offset=0):
    """Search both movie and series DBs and merge results as objects."""
    q = {'$text': {'$search': query}} if query else {}
    if file_type:
        q['file_type'] = file_type
    movie_cursor = movie_db.find(q).skip(offset).limit(max_results)
    series_cursor = series_db.find(q).skip(offset).limit(max_results)
    movie_results = [SimpleNamespace(**doc) async for doc in movie_cursor]
    series_results = [SimpleNamespace(**doc) async for doc in series_cursor]
    results = movie_results + series_results
    next_offset = offset + len(results)
    return results, next_offset

# Referral/user logic
async def get_user(user_id):
    return await user_db.find_one({'user_id': user_id})

async def add_user(user_id, referrer=None):
    user = await get_user(user_id)
    if not user:
        await user_db.insert_one({
            'user_id': user_id,
            'referrals': [],
            'ref_count': 0,
            'referrer': referrer,
            'active': False
        })
        if referrer:
            await user_db.update_one(
                {'user_id': referrer},
                {'$addToSet': {'referrals': user_id}, '$inc': {'ref_count': 1}}
            )

async def activate_user(user_id):
    await user_db.update_one({'user_id': user_id}, {'$set': {'active': True}})

async def is_user_active(user_id):
    user = await get_user(user_id)
    if not user:
        return False
    if not ENABLE_REFERRAL:
        return True
    return user.get('active', False)

async def check_and_activate(user_id):
    """Check if user meets referral requirement and activate if so."""
    user = await get_user(user_id)
    if user and user.get('ref_count', 0) >= REQUIRED_REFERRALS:
        await activate_user(user_id)
        return True
    return False

async def get_total_counts():
    """Return total file counts for movies, series, and combined."""
    movie_count = await movie_db.count_documents({})
    series_count = await series_db.count_documents({})
    return movie_count, series_count, movie_count + series_count
