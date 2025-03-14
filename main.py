# Python модули
from pyrogram import Client, filters
from pyrogram.types import ReactionTypeCustomEmoji


# Локальные модули
from config import API_ID, API_HASH, TARGET_USER_ID
from logger import logger


# Переменные
app = Client("reaction_user", api_id=API_ID, api_hash=API_HASH)

REACTIONS = [
    ReactionTypeCustomEmoji(custom_emoji_id=5386357247993462889),
    ReactionTypeCustomEmoji(custom_emoji_id=5386713588545112771),
    ReactionTypeCustomEmoji(custom_emoji_id=5388970155772496192)
]


# Функции
@app.on_message(filters.user(TARGET_USER_ID))
async def handle_messages(_, message):
    try:
        await app.set_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            reaction=REACTIONS
        )
        logger.info(f'USER={message.from_user.id}, MESSAGE="reactions set on {message.id} in {message.chat.id}"')
    except Exception as e:
        logger.error(f'USER={message.from_user.id}, MESSAGE="{e}"')


if __name__ == '__main__':
    app.run()
