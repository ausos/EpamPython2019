"""

Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:

* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса


>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(pool))
2
>>> del unit3
>>> print(len(pool))
1

"""
class Meta(type):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = {}

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args, **kwargs)
            self.__cache[args] = obj
            return obj
        
class SiamObj(metaclass=Meta):
    def __init__(self, *arg, **kwargs):
        self.arg = arg
        self.kwargs = kwargs

unit1 = SiamObj('1', '2', a=1)
unit2 = SiamObj('1', '2', a=1)
unit1 is unit2
