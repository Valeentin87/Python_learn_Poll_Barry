
word = input('введите слово: ')

def search4vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = set(vowels).intersection(set(words))
    print(''.join(list(i)))
    
search4vowels(word)