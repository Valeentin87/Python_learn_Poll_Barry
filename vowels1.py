# программа определяет вхождение гласной буквы в слово только один раз
vowels = ['a', 'e', 'i', 'o', 'u']   # список гласных
vowels_now = []   # список гласных, которые войдут в наше слово
word = 'aaaapple'   # слово, в котором будем проверять вхождение гласных
for i in word:
    if i in vowels:
        if i not in vowels_now:
            vowels_now.append(i)
print(vowels_now)

