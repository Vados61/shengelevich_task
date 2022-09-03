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

lector_skills = [
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
]


class Student:

    def __init__(self, name):
        self.name = name
        self.lector_pull = ()

    def matching(self):
        pass


class Lector:

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


students = [Student(student) for student in student_list]
lectors = [Lector(lector, random.sample(lector_skills, 2)) for lector in lector_list]

# Привет Хуцкар