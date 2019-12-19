"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго, проверку делаю автотестами и просмотром кода.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict

class DeadlineError(Exception):
    """The deadline has already expired"""

class Person:
    """Created new person"""
    __slots__ = ['last_name', 'first_name']

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

class Student(Person):
    """Created when new student registers"""

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError('You are late')

class Homework:
    """Created when adding new homework"""
    __slots__ = ['text', 'deadline', 'created']

    def __init__(self, text, days):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days)

    def is_active(self):
        return datetime.datetime.now() - self.created <= self.deadline

class HomeworkResult:

    __slots__ = ['author', 'homework', 'solution', 'created']

    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object') 
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()

class Teacher(Person):
    """Created when new teacher registers"""
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, days):
        return Homework(text, days)

    def check_homework(self, hw_result):
        if len(hw_result.solution) > 5:
            self.homework_done[hw_result.homework].add(hw_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            cls.homework_done[homework].clear()
        else:
            cls.homework_done.clear()

if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
