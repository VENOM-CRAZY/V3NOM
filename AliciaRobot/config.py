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

    TOKEN = "1738957760:AAE-1EK1YNXygAVNh8iWgb_VvmKXp3KqWCI"

    try:
        OWNER_ID = 2079458478
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = -1001728598713
    OWNER_USERNAME = "VENOMxCRAZY"
    EVENT_LOGS = -1001728598713
    URL = "https://aliciarobot.herokuapp.com/"
    PORT = 5000
    API_ID = 17945559
    API_HASH = "3dfcedf92c63b783ca849ac27a6f9e27"
    DB_URI = "postgres://ovvvetip:7bnUn0fLFD6SN945S1r0klG73lPZjDEI@fanny.db.elephantsql.com/ovvvetip"
    MONGO_DB_URI = "mongodb+srv://ZAID3:ZAID3@cluster0.nb30b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    BOT_ID = 1738957760
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
    TOKEN = "1738957760:AAE-1EK1YNXygAVNh8iWgb_VvmKXp3KqWCI"
    SUPPORT_CHAT = "V3NOM_Support"
    SPAMWATCH_API = "HYx~bySNWNSftcL3O_z9h5qHJGK2OSi0WnRKC7nIAtlLFKPXid4wGtnFiePwjmmw"
    REDIS_URL = "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559"
    STRING_SESSION = "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI="

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

    TOKEN = "1738957760:AAE-1EK1YNXygAVNh8iWgb_VvmKXp3KqWCI"

    try:
        OWNER_ID = 2079458478
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = -1001728598713
    OWNER_USERNAME = "VENOMxCRAZY"
    EVENT_LOGS = --1001728598713
    URL = "https://aliciarobot.herokuapp.com/"
    PORT = 5000
    API_ID = 17945559
    API_HASH = "3dfcedf92c63b783ca849ac27a6f9e27"
    DB_URI = "postgres://ovvvetip:7bnUn0fLFD6SN945S1r0klG73lPZjDEI@fanny.db.elephantsql.com/ovvvetip"
    MONGO_DB_URI = "mongodb+srv://ZAID3:ZAID3@cluster0.nb30b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    BOT_ID = 1613196478
    NO_LOAD = "rss"
    STRICT_GBAN = True
    ALLOW_EXCL = True
    TOKEN = "1738957760:AAE-1EK1YNXygAVNh8iWgb_VvmKXp3KqWCI"
    SUPPORT_CHAT = "V3NOM_Support"
    SPAMWATCH_API = "HYx~bySNWNSftcL3O_z9h5qHJGK2OSi0WnRKC7nIAtlLFKPXid4wGtnFiePwjmmw"
    REDIS_URL = "redis://:pf5a846bd88f2da1b37e94c9a66af70d4413d6a9af501d251661fc66d2bac54f8@ec2-34-227-200-242.compute-1.amazonaws.com:24559"
    STRING_SESSION = "1AZWarzsBu4JME17PtDItxFthl0IJ0WBrnkP8EyL7Wk-G9xw8ysL40HvXZguTOLXc6IRXhbehHL7rSzPRc-AhT4Q5bbLj7VAYKda_d-TBcdckJZENCOD4daN8xGDX41m_sTRwXBBvYJg7M3OJywow_nN89TfbEu1Ui3jAS46Heom1QLdw9n5Aewm9zxjQrWF_99fZIlYId-Akoz7FxA88TKOC_NJDwt_ST-u6xAQJNhXcUxfuewoEOtyGuoMezi5v5bIMTBiGNKkojlxHCHS2qnNCQYlBLiklIS_xGVPbdDw95JPAYfgwNRgPMUaBvXyu3Qd_4iGIIoL-riBZJ923fCO9m-bZRFI="
    ALLOW_CHATS = True
    TIGERS = 2079458478
    WOLVES = 2079458478
    DEMONS = 2079458478
    DEV_USERS = 2079458478
    DRAGONS = 2079458478
    BL_CHATS = None
