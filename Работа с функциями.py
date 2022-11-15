
# ----------можно добавлять аннотацию к функции, которая будет определять тип аргумента и тип возвращаемых значений----------

def search4vowels(words: str) -> set:
    '''возвращает множество гласных в слове, являющемся аргументом'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = set(vowels).intersection(set(words))
    return i
print(help(search4vowels))

#----------функции, принимающие 2 аргумента на вход----------------

word = input('введите слово: ')
chars_1 = input('введите буквы, которые ищем: ')

def search4letters(phrase: str, letters: str) -> set:
    '''возвращает множество букв из второго аргумента, встречающихся в фразе'''
    i = set(letters).intersection(set(phrase))
    return i


result = search4letters(word, chars_1)
print(result)