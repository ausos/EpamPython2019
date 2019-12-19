""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:

    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, e_type, e_inst, e_tb):
        return issubclass(e_type, self.exceptions)

with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
