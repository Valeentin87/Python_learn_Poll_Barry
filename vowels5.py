

# ------------создадим программу, которая с помощью словаря будет показыывать сколько раз встречается в слове та или иная гласная---------
vowels = ['a', 'e', 'i', 'o', 'u']   # список наших гласных
word = list(input('введите слово с гласными: '))
found = {}  # пустой словарь, в котором будем накапливать наши гласные

for i in word:
    if i in vowels:
        found.setdefault(i, 0)
        found[i] +=1
for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time (s).')


    

