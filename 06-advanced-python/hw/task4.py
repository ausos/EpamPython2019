"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self, lvl=0):

        out = f'V {self.name}\n'
        if isinstance(self.content, PrintableFile):
            out += f'{"|   " * lvl}|-> {self.content.__str__(lvl + 1)}'
        else:
            for item in self.content:
                out += f'{"|   " * lvl}|-> {item.__str__(lvl + 1)}'
        return out

    def __contains__(self, item):
        for el in self.content:
            if item.name == el.name:
                return True
            elif hasattr(el, 'content'):
                return el.__contains__(item)


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self, lvl=0):
        return f'{self.name}\n'

file1 = PrintableFile('file1')
file2 = PrintableFile('file2')
file3 = PrintableFile('file3')
file4 = PrintableFile('file4')
folder4 = PrintableFolder('folder4', [file3])
folder3 = PrintableFolder('folder3', [file3])
folder2 = PrintableFolder('folder2', [folder3, file2])
folder1 = PrintableFolder('folder1', [folder2, file1])
print(folder1)
print(file3 in folder2)
