import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 18050628))
    API_HASH = os.environ.get("API_HASH", "89f8ac516563145c27a185d280fdcb01")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6077015920:AAGrwuQyIWIHq_64755SJRinu0c1HWvYIhM")
    OWNER_ID = int(os.environ.get('OWNER_ID', 5165442029)) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "-1001877236737").split()] # if open to everyone give 0
    AUTH_IDS.append(OWNER_ID)
    QOBUZ_MAIL = os.environ.get("QOBUZ_MAIL", "natamalceva80@netek.me")
    QOBUZ_PASS = os.environ.get("QOBUZ_PASS", "Qobuz2023")
    QOBUZ_QUAL = int(os.environ.get("QOBUZ_QUAL", 27))
    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY', None)
    HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', None)
    UPDATE_ALL = bool(os.environ.get("UPDATE_ALL", True))
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001821015909")
    botStartTime = time.time() # dont touch
