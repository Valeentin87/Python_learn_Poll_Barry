from flask import Flask   # импортируем класс Flask из модуля flask
from vsearch import search4letters


app = Flask(__name__)    # создание экземпляра объекта Flask и присваивание его переменной app

@app.route('/')     # декоратор функции настраивает поведение функции без изменения кода самой функции, функция становится декорированной
def hello() -> str:         # декоратор route через переменную app позволяет связать веб-путь URL c функцией на Python
    return 'Hello world from Flask!'  # далее декоратор route возвращает результат выполнения функции ожидающему веб серверу, а тот в свою очередь веб-браузеру

@app.route('/search4')
def do_search() -> str:
    '''Функция возвращает через декоратор веб-серверу localhost(127.0.0.1) а тот в свою очередь веб браузеру
    результат работы функции search4letters из созданного нами ранее модуля vsearch при обращении по URL localhost/search '''
    result_set = search4letters('life, the universe, and everything!', 'eiru,!')
    result_str = ''.join(list(result_set))
    return result_str
app.run()   # предлагает объекту Flask запустить веб-сервер в переменной app используя метод run