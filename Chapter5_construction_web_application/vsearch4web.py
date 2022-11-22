from flask import Flask, render_template, request, redirect, escape   # импортируем класс Flask из модуля flask
from vsearch import search4letters


app = Flask(__name__)    # создание экземпляра объекта Flask и присваивание его переменной app

#@app.route('/')     # декоратор функции настраивает поведение функции без изменения кода самой функции, функция становится декорированной
#def hello() -> '302':         # декоратор route через переменную app позволяет связать веб-путь URL c функцией на Python
#    return redirect('/entry')  # далее декоратор route возвращает результат выполнения функции ожидающему веб серверу, а тот в свою очередь веб-браузеру


#@app.route('/search4', methods=['POST'])
#def do_search() -> 'html':
    # Функция возвращает через декоратор веб-серверу localhost(127.0.0.1) а тот в свою очередь веб браузеру
    # результат работы функции search4letters из созданного нами ранее модуля vsearch при обращении по URL localhost/search '''
#    phrase = request.form['phrase']
#    letters = request.form['letters']
#    result_set = search4letters(phrase, letters)
#    result_str = ''.join(list(result_set))
#    return result_str

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
        return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a', encoding='utf-8') as data:
        print(req.form,req.remote_addr,req.user_agent, res, file=data, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    '''Функция возвращает html страницу 'results.html' в которую в качестве аргументов вставляются фраза которую ввел
    пользователь, буквы, которые ищем в фразе, буквы, которые нашли и название страницы'''
    phrase = request.form['phrase']
    letters = request.form['letters']
    result_set = search4letters(phrase, letters)
    result_str = ''.join(list(result_set))
    log_request(request, result_str)  # вызов функции, позволяющей документировать вводимые запросы и результаты
    title = 'Here are your results'
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_title = title, the_results = result_str)

@app.route('/viewlog')
def view_log() -> str:
    with open('vsearch.log') as log:
        contents=log.read()
    return escape(contents)

if __name__=="__main__":
    app.run(debug=True)   # предлагает объекту Flask запустить веб-сервер в переменной app используя метод run debug=True -
                        # режим отладки



