"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

INGREDIENTS = {'eggs': 2, 'flour': 300, 'milk': 0.5,
               'sugar': 100, 'oil': 10, 'butter': 120}


class Fridge:
    def __init__(self, eggs, flour, milk, sugar, oil, butter):
        self._eggs = eggs
        self._flour = flour
        self._milk = milk
        self._sugar = sugar
        self._oil = oil
        self._butter = butter


class EggsHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._eggs < INGREDIENTS['eggs']:
            eggs_to_add = INGREDIENTS['eggs'] - fridge._eggs
            print(f"{eggs_to_add} eggs needed")
        else:
            print('enough eggs')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class FlourHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._flour < INGREDIENTS['flour']:
            flour_to_add = INGREDIENTS['flour'] - fridge._flour
            print(f"{flour_to_add} grams of flour needed")
        else:
            print('enough flour')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class MilkHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._milk < INGREDIENTS['milk']:
            milk_to_add = INGREDIENTS['milk'] - fridge._milk
            print(f"{milk_to_add} liters of milk needed")
        else:
            print('enough milk')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class SugarHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._sugar < INGREDIENTS['sugar']:
            sugar_to_add = INGREDIENTS['sugar'] - fridge._sugar
            print(f"{sugar_to_add} grams of sugar needed")
        else:
            print('enough sugar')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class OilHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._oil < INGREDIENTS['oil']:
            oil_to_add = INGREDIENTS['oil'] - fridge._oil
            print(f"{oil_to_add} milliliters of oil needed")
        else:
            print('enough oil')
        if self._next_handler:
            return self._next_handler.handle(fridge)


class ButterHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._butter < INGREDIENTS['butter']:
            butter_to_add = INGREDIENTS['butter'] - fridge._butter
            print(f"{butter_to_add} grams of butter needed")
        else:
            print('enough butter')
        if self._next_handler:
            return self._next_handler.handle(fridge)


def fill_fridge(fridge):
    eggs_handler = EggsHandler()
    flour_handler = FlourHandler()
    milk_handler = MilkHandler()
    sugar_handler = SugarHandler()
    oil_handler = OilHandler()
    butter_handler = ButterHandler()

    eggs_handler.set_next(flour_handler).set_next(milk_handler).set_next(
        sugar_handler).set_next(oil_handler).set_next(butter_handler)

    eggs_handler.handle(fridge)


fridge = Fridge(eggs=2, flour=200, milk=0.5, sugar=90, oil=5, butter=100)
print(fill_fridge(fridge))
