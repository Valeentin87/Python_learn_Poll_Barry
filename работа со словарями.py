# ------------создание словарей через пары ключ - значение -----------------
# person3 = { 'Name': 'Ford Prefect', 'Gender': 'Male', 'Occupation': 'Researcher',
#             'Home Planet': 'Betelgeuse Seven'}
# 
# print(person3)  # словарь выводится в консоль не в той последовательности, в которой в него вводились данные
# 
# print(person3['Gender'])  # возможно обращение к каждому элементу словаря по ключу, будет выдавать соответствующее ему значение
# 
# person3['Age'] = 33  # добавление новой пары ключ-значение в словарь
# 
# print(person3)
# 
# for keys in person3:
#     print(keys)      # вывод в консоль всех ключей словаря
#     
# for keys in person3:
#     print(person3[keys])  # вывод в консоль всех значений соответствующих ключам в словаре
#     
#     for key in sorted(person3):
#         print(key)     # упорядочение по алфавиту ключей словаря

fruits = {}
fruits.setdefault('apple', 0) # метод позволяет добавить в словарь новую пару ключ - значение, если ключа не существовало и присвоить ему новое значение
# по сути заменяет две строки кода  if apple not in fruits:
                                    #	fruits[apple] = 0
fruits.setdefault('orange', 0)
print(fruits)

    

    



