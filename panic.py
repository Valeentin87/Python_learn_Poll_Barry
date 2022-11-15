# -------------в этой задаче из фразы Don't panic! с помощью методов строк получить 'on tap'

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.remove('D')
plist.remove("'")

plist.pop(9)
plist.pop(8)
plist.pop(7)
plist.pop(6)
plist.pop(1)
plist.insert(1, 'n')
plist.insert(2, ' ')
plist.remove('a')
plist.pop(4)
plist.insert(4, 'a')
print(plist)

new_phrase = ''.join(plist)

print(new_phrase)