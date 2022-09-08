"""
1. нужно выбрать и сделать импорт модуля для работы с ботом
2. сделать нормальные теги
3. сделать нормальные имена лекторов и увеличить их колличество
4. реализовать логику диалога бота с пользователем
"""
import asyncio
import random
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

from data import *


class UserState(StatesGroup):
    name = State()
    change_tags = State()
    change_lector = State()


storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def user_register(message: types.Message):
    await message.answer("Для записи к лектору введите команду: /reg боту в лс")


@dp.message_handler(commands=['reg'])
async def user_register(message: types.Message):
    await message.answer("Как вас записать?")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    answer = "Введите через пробел три номера предпочтительных  навыков:"
    for id, item in enumerate(lector_tags):
        answer += f'\n{id + 1}. {item}'
    await message.answer(answer)
    await UserState.next()


@dp.message_handler(state=UserState.change_tags)
async def change_tags(message: types.Message, state: FSMContext):
    user_indexes = [int(item) - 1 for item in message.text.split()]
    user_tags = set()
    for id, tag in enumerate(lector_tags):
        if id in user_indexes:
            user_tags.add(tag)
    await state.update_data(usertags=user_tags)
    answer = 'По вашим критериям подходят следущие лекторы:'
    for lector in lectors:
        if lector.cheak_matching(user_tags):
            answer += lector.cheak_matching(user_tags)
    answer += '\nВведите имя выбранного лектора'
    await message.answer(answer)
    await UserState.next()


@dp.message_handler(state=UserState.change_lector)
async def change_lector(message: types.Message, state: FSMContext):
    name_lector = message.text
    await state.update_data(userlector=name_lector)
    data = await state.get_data()
    for lector in lectors:
        if lector.name == name_lector:
            lector.matching(name_lector)
            answer = f"Спасибо, {data['username']}" \
                     f"\nВы записаны к лектору {data['userlector']}"
            await message.answer(answer)
            await state.finish()


class Lector:

    def __init__(self, name, tags):
        self.name = name
        self.tags = set(tags)
        self.student_pull = set()

    def cheak_matching(self, tegs):
        if self.tags & tegs:
            teg = []
            for i in self.tags:
                teg.append(i)
            return f'\n{self.name} с навыками: {teg[0]} и {teg[1]}'

    def matching(self, student):
        self.student_pull.add(student)


lectors = [Lector(lector, random.sample(lector_tags, 2)) for lector in lector_list]


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
