# from pa.app import *
from vol.vkbot import *
from rom.bot import *
from threading import Thread

th_bot = Thread(target=bot, args=())
th_userbot = Thread(target=botik, args=())

th_userbot.start()
th_bot.start()
