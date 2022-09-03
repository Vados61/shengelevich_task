'''
1. нужно выбрать и сделать импорт модуля для работы с ботом
2. сделать нормальные теги
3. сделать нормальные имена лекторов и увеличить их колличество
4. реализовать логику диалога бота с пользователем
'''

import random


lector_list = [
    'lector_Вася',
    'lector_Петя',
    'lector_Коля',
    'lector_Саша',
    'lector_Ваня',
    'lector_Леша',
    'lector_Ваня',
    'lector_Юра',
    'lector_Володя',
    'lector_Паша',
    'lector_Даня',
    'lector_Сережа',
    'lector_Женя',
    'lector_Лена',
    'lector_Катя',
    'lector_Даша',
    'lector_Света',
    'lector_Маша',

]
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

lector_tegs = {
     'skill_быстрый',
    'skill_сильный',
    'skill_смелый',
    'skill_высокий',
    'skill_красивый',
    'skill_умный',
    'skill_ловкий',
    'skill_хитрый',
    'skill_дальновидный',
    'skill_образованый',
    'skill_храбрый',
    'skill_лютый',
    'skill_веселый',
    'skill_увереный',
    'skill_спокойный',
    'skill_холоднокровный',
    'skill_авторитарный',
    'skill_дисциплинированный',
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
