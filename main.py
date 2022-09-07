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
    print('1')
    answer = "Введите через пробел три предпочтительных навыка:"
    for id, item in enumerate(lector_tags):
        answer += f'\n{id + 1}. {item}'
    await message.answer(answer)


@dp.message_handler()
async def send_matching_result(message: types.Message):
    tags = set(message.text.split(' '))
    answer = 'По вашим критериям подходят следущие лекторы:'
    for lector in lectors:
        if lector.cheak_matching(tags):
            answer += lector.cheak_matching(tags)
    await message.answer(answer)


class Student:

    def __init__(self, name):
        self.name = name
        self.lector_pull = ()


class Lector:

    def __init__(self, name, tags):
        self.name = name
        self.tags = set(tags)

    def cheak_matching(self, tegs):
        if self.tags & tegs:
            teg = []
            for i in self.tags:
                teg.append(i)
            return f'\n{self.name} с навыками: {teg[0]} и {teg[1]}'


lectors = [Lector(lector, random.sample(lector_tags, 2)) for lector in lector_list]

# tegs = set(random.sample(lector_tegs, 3))
#
# for lector in lectors:
#
#     if lector.cheak_matching(tegs):
#         print(lector.cheak_matching(tegs))

if __name__ == '__main__':
    executor.start_polling(dp)
