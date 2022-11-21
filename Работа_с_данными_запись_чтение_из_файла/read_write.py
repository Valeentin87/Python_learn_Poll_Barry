# работа с данными (чтение из файла, запись в файл, дозапись в конец файла)
# работа в режиме записи данных в конец файла

tasks=open('Task.txt', 'a', encoding='utf-8')  # создали файловый поток tasks, который позволяет записывать в конец файла 'Task.txt'
                             # при этом, если файла не было, то он создаётся
print('Сходить в магазин', file=tasks) #записываем данные в файловый поток
print('Выгулять собаку', file=tasks)
print('Постирать вещи', file=tasks)
tasks.close() # закрыли файловый поток и работу с файлом
