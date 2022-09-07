"""
1. нужно выбрать и сделать импорт модуля для работы с ботом
2. сделать нормальные теги
3. сделать нормальные имена лекторов и увеличить их колличество
4. реализовать логику диалога бота с пользователем
"""

import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor

from data import *


class UserState(StatesGroup):
    name = State()
    change_tags = State()
    change_lector = State()


TOKEN = "5562333620:AAFEDZ2_5EWbPOWPEbrZwVKlfOo-X0MRYmw"
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['reg'])
async def user_register(message: types.Message):
    await message.answer("Введите своё имя")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    answer = "Введите через пробел три предпочтительных навыка:"
    for id, item in enumerate(lector_tags):
        answer += f'\n{id + 1}. {item}'
    await message.answer(answer)
    await UserState.next()


@dp.message_handler(state=UserState.change_tags)
async def change_tags(message: types.Message, state: FSMContext):
    user_tags = set(message.text.split())
    await state.update_data(usertags=user_tags)
    answer = 'По вашим критериям подходят следущие лекторы:'
    for lector in lectors:
        if lector.cheak_matching(user_tags):
            answer += lector.cheak_matching(user_tags)
    await message.answer(answer)
    await UserState.next()


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

if __name__ == '__main__':
    executor.start_polling(dp)
