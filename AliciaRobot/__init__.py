import logging
import os
import sys
import time
import spamwatch

import telegram.ext as tg
from redis import StrictRedis
from pyrogram import Client, errors
from telethon import TelegramClient
from telethon.sessions import StringSession
from Python_ARQ import ARQ
from aiohttp import ClientSession



StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)


# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", "1613196478:AAHzs8A_73OkOBISpQ5emx5ToDxMlJu0XmU")

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", 1212368262))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", -1001204088829)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "H1M4N5HU0P")

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", -1001459323267)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "https://aliciarobot.herokuapp.com/")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", 2857558)
    API_HASH = os.environ.get("API_HASH", "1038be815e038592fa2b483c13dd6c4b")
    BOT_ID = int(os.environ.get("BOT_ID", 1613196478))
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://vhyrades:gOlW9HnB8gjo80BKZMKLdQucme9Si2nB@fanny.db.elephantsql.com/vhyrades")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://AliciaRobotOP:AliciaRobotOP@cluster0.pfhfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DONATION_LINK = os.environ.get("DONATION_LINK")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "rss").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", "-xyz")
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "MafiaBot_Support")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", "sJsaTYZnYqTR7z~pq8OAdVj2UIktizitY5k6ivnErXkArICQv_ZbNmG6HMDlE7Lg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI=")
    REDIS_URL = os.environ.get("REDIS_URL", "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559")
    ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://thearq.tech")
    ARQ_API_KEY = os.environ.get("ARQ_API_KEY", "NAQKZO-UMQSBG-IUTXPK-WZRJDB-ARQ")

 
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

    if STRING_SESSION:
        ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
    else:
        sys.exit(1)

    try:
        ubot.start()
    except BaseException:
        print("Network Error/INVALID TOKEN !")
        sys.exit(1)
        


    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")


else:
    from AliciaRobot.config import Development as Config

    TOKEN = "1613196478:AAHzs8A_73OkOBISpQ5emx5ToDxMlJu0XmU"

    try:
        OWNER_ID = 1212368262
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = -1001204088829
    OWNER_USERNAME = "H1M4N5HU0P"

    EVENT_LOGS = -1001459323267
    URL = "https://aliciarobot.herokuapp.com/"
    PORT = 5000
    API_ID = 2857558
    API_HASH = "1038be815e038592fa2b483c13dd6c4b"

    DB_URI = "postgresql://vhyrades:gOlW9HnB8gjo80BKZMKLdQucme9Si2nB@fanny.db.elephantsql.com/vhyrades"
    MONGO_DB_URI = "mongodb+srv://AliciaRobotOP:AliciaRobotOP@cluster0.pfhfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    BOT_ID = 1613196478
    NO_LOAD = "rss"
    STRICT_GBAN = True
    ALLOW_EXCL = True
    TOKEN = "1613196478:AAHzs8A_73OkOBISpQ5emx5ToDxMlJu0XmU"
    SUPPORT_CHAT = "MafiaBot_Support"
    WORKERS = 8
    SPAMWATCH_API = "sJsaTYZnYqTR7z~pq8OAdVj2UIktizitY5k6ivnErXkArICQv_ZbNmG6HMDlE7Lg"
    REDIS_URL = "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559"
    STRING_SESSION = "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI="
    try:
        DRAGONS = set(int(x) for x in [])
        DEV_USERS = set(int(x) for x in [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")


DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1868387344)
DEV_USERS.add(1212368262)
DEV_USERS.add(1936648846)
DEV_USERS.add(1957781414)
DEV_USERS.add(1949856187)
DRAGONS.add(2118437554)
DRAGONS.add(1709002409)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")


aiohttpsession = ClientSession()


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("alicia", API_ID, API_HASH)
pbot = Client("aliciaPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
dispatcher = updater.dispatcher


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)



# Load at end to ensure all prev variables have been set
from AliciaRobot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
