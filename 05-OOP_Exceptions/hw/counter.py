"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls_counter = 0
    class_init = cls.__init__

    def __init__(self, *args, **kwargs):
        class_init(self, *args, **kwargs)
        nonlocal cls_counter
        cls_counter += 1

    @classmethod
    def get_created_instances(cls):
        nonlocal cls_counter 
        return cls_counter

    @classmethod
    def reset_instances_counter(cls):
        nonlocal cls_counter 
        previous_value = cls_counter
        cls_counter = 0
        return previous_value

    cls.__init__ = __init__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
