import string


def letters_range(start, stop=None, step=1, **changes):

    abc = list(string.ascii_lowercase)
    for i in changes:
        abc[abc.index(i)] = changes[i]

    if stop is None:
        return abc[:abc.index(start):step]
    else:
        return abc[abc.index(start):abc.index(stop):step]

print(letters_range('b', 'w', 2))
print(letters_range('g'))
print(letters_range('g', 'p'))
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
print(letters_range('p', 'g', -2))
print(letters_range('a'))
