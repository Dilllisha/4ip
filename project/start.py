# from pa.app import *
from vol.vkbot import *
from rom.bot import *
from asyncio import create_task, run

async def main():
    task_1 = create_task(bot(chat_gpt_button,weather_button).start())
    task_2 = create_task(botik().start())

    await task_1
    await task_2

if __name__ == '__main__':
    run(main())
