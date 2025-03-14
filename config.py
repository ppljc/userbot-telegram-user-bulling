# Python модули
from dotenv import load_dotenv

import os


# Чтение переменных окружения из .env файла
load_dotenv(override=True)

API_HASH = os.environ['API_HASH']
API_ID = os.environ['API_ID']
TARGET_USER_ID = int(os.environ['TARGET_USER_ID'])
