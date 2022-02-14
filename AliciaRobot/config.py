# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/AliciaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    TOKEN = "5200251156:AAHDycWFf0PiV-eOyTeC61afx75p2-gxzNA"

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
    ALLOW_CHATS = True
    TIGERS = ""
    WOLVES = ""
    DEMONS = ""
    DEV_USERS = ""
    DRAGONS = ""
    BL_CHATS = None
    ALLOW_EXCL = True
    TOKEN = "5200251156:AAHDycWFf0PiV-eOyTeC61afx75p2-gxzNA"
    SUPPORT_CHAT = "MafiaBot_Support"
    SPAMWATCH_API = "sJsaTYZnYqTR7z~pq8OAdVj2UIktizitY5k6ivnErXkArICQv_ZbNmG6HMDlE7Lg"
    REDIS_URL = "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559"
    STRING_SESSION = "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI="

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

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
    TOKEN = "5200251156:AAHDycWFf0PiV-eOyTeC61afx75p2-gxzNA"
    SUPPORT_CHAT = "MafiaBot_Support"
    SPAMWATCH_API = "sJsaTYZnYqTR7z~pq8OAdVj2UIktizitY5k6ivnErXkArICQv_ZbNmG6HMDlE7Lg"
    REDIS_URL = "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559"
    STRING_SESSION = "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI="
    ALLOW_CHATS = True
    TIGERS = 1212368262
    WOLVES = 1212368262
    DEMONS = 1212368262
    DEV_USERS = 1212368262
    DRAGONS = 1212368262
    BL_CHATS = None
