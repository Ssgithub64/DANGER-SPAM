import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 23418117
API_HASH = "e93479e4b3eae090bf90a978b14ffc09"
CMD_HNDLR = getenv(".", default=".")
HEROKU_APP_NAME = getenv("danger47", None)
HEROKU_API_KEY = getenv("HRKU-8229ca76-ef2f-45da-bd9d-6985de5e50ae", None)

BOT_TOKEN = getenv("7218510765:AAE74uJ7K0ZhFidNJ9B3gEXJiQQMmCz5R1M", default=None)
BOT_TOKEN2 = getenv("6933749283:AAHXfeaOYN6GRq6ulwh6h_t3okU1fJ9O9ow", default=None)
BOT_TOKEN3 = getenv("6941963882:AAG83xVPWGCnAZ3p6FbVkPGO6ePy35GZTtY", default=None)
BOT_TOKEN4 = getenv("7418458917:AAHqoEIOLryX-tB7xAuMzB9QQDRhhtrsrVY", default=None)
BOT_TOKEN5 = getenv("7404154221:AAEakbPFVjBJvCwgR202ug7t96AZBXeAggg", default=None)
BOT_TOKEN6 = getenv("7373171347:AAFxkSmJRQtezNxwQBp-M0oE3Sajm_753RI", default=None)
BOT_TOKEN7 = getenv("7305524797:AAExa-PiW8TCV13FwFy71wqIjAwUws17rio", default=None)
BOT_TOKEN8 = getenv("7266931821:AAFIhecxMR-xbRaX_9Q2meBVldmrxsVuRLQ", default=None)
BOT_TOKEN9 = getenv("6942874484:AAEboLYlFk0LZUjhbTibVOtAoY0xscka37Y", default=None)
BOT_TOKEN10 = getenv("7486814175:AAHzomTHUXeCqGpqTtCTPwyBLDrWRLLNuqU", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("6063555621", default="6063555621").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("1331161476", default="5867944994"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
