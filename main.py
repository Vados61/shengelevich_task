'''
1. нужно выбрать и сделать импорт модуля для работы с ботом
2. сделать нормальные теги
3. сделать нормальные имена лекторов и увеличить их колличество
4. реализовать логику диалога бота с пользователем
'''
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from data import *

TOKEN = "5562333620:AAFEDZ2_5EWbPOWPEbrZwVKlfOo-X0MRYmw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f"Для вас доступны преподаватели с навыками {lector_tegs}")


class Student:

    def __init__(self, name):
        self.name = name
        self.lector_pull = ()


class Lector:

    def __init__(self, name, tegs):
        self.name = name
        self.tegs = set(tegs)

    def cheak_matching(self, tegs):
        if self.tegs & tegs:
            teg = []
            for i in self.tegs:
                teg.append(i)
            return f'Вам подошел {self.name} с навыками: {teg[0]} и {teg[1]}'


lectors = [Lector(lector, random.sample(lector_tegs, 2)) for lector in lector_list]

tegs = set(random.sample(lector_tegs, 3))

for lector in lectors:

    if lector.cheak_matching(tegs):
        print(lector.cheak_matching(tegs))

if __name__ == '__main__':
    executor.start_polling(dp)
