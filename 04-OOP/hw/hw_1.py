import datetime


class Homework():
    """Created when adding new homework"""
    __slots__ = ['text', 'deadline', 'created']

    def __init__(self, text, days):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days)

    def is_active(self):
        return datetime.datetime.now() - self.created <= self.deadline


class Student():
    """Created when new student registers"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if homework.is_active() is True:
            return homework
        else:
            print('You are late')
            return


class Teacher():
    """Created when new teacher registers"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, days):
        self.text = text
        self.days = days
        homework = Homework(self.text, self.days)
        return homework


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late