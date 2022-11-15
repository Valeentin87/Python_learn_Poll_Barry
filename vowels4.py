# программа определяет вхождение гласной буквы в слово только один раз
# vowels = ['a', 'e', 'i', 'o', 'u']   # список гласных
# vowels_now = []   # список гласных, которые войдут в наше слово
# word = list(input('введите слово  '))   # слово, в котором будем проверять вхождение гласных
# for i in word:
#     if i in vowels:
#         if i not in vowels_now:
#             vowels_now.append(i)
# print(vowels_now)

# ------------создадим программу, которая с помощью словаря будет показыывать сколько раз встречается в слове та или иная гласная---------
vowels = ['a', 'e', 'i', 'o', 'u']   # список наших гласных
word = list(input('введите слово с гласными: '))
found = {}  # пустой словарь, в котором будем накапливать наши гласные

for i in word:
    if i in vowels:
        found[i] +=1
for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time (s).')


    


