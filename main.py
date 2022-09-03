'''
1. нужно выбрать и сделать импорт модуля для работы с ботом
2. сделать нормальные теги
3. сделать нормальные имена лекторов и увеличить их колличество
4. реализовать логику диалога бота с пользователем
'''

import random

student_list = [
    'sudent_1',
    'sudent_2',
    'sudent_3',
    'sudent_4',
    'sudent_5',
    'sudent_6',
    'sudent_7',
    'sudent_8',
    'sudent_9',
    'sudent_10'
]

lector_list = [
    'lector_1',
    'lector_2',
    'lector_3',
    'lector_4',
    'lector_5'
]

lector_tegs = {
    'skill_1',
    'skill_2',
    'skill_3',
    'skill_4',
    'skill_5',
    'skill_6',
    'skill_7',
    'skill_8',
    'skill_9',
    'skill_10'
}


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
            return f'Вам подошел {self.name} с навыками:{teg[0]} и {teg[1]}'


students = [Student(student) for student in student_list]
lectors = [Lector(lector, random.sample(lector_tegs, 2)) for lector in lector_list]

tegs = set(random.sample(lector_tegs, 3))

for lector in lectors:

    if lector.cheak_matching(tegs):
        print(lector.cheak_matching(tegs))
