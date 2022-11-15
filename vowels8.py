
# word = input('введите слово: ')
# 
# def search4vowels(words):
#     '''выводит в консоль все гласные без повторений,
# имеющиеся во введенном в консоль слове'''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     i = set(vowels).intersection(set(words))
#     print(''.join(list(i)))
#     
# search4vowels(word)

#--------------------------------------------------------

# word = input('введите слово: ')
# 
# def search4vowels(words):
#     '''возвращает булевое значение в зависимости есть хотя бы одна гласная или нет'''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     i = set(vowels).intersection(set(words))
#     return bool(i)
#     
# print(search4vowels(word))

#--------------------------------------------------------

# word = input('введите слово: ')
# 
# def search4vowels(words):
#     '''возвращает булевое значение в зависимости есть хотя бы одна гласная или нет'''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     i = set(vowels).intersection(set(words))
#     return i
#     
# print(search4vowels(word))

#---------------------------------------------------------

word = input('введите слово: ')
chars_1 = input('введите буквы, которые ищем: ')

def search4letters(phrase: str, chars: str) -> set:
    '''возвращает множество букв из второго аргумента, встречающихся в фразе'''
    i = set(chars).intersection(set(phrase))
    return i
result = search4letters(word, chars_1)
print(result)