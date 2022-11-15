from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

app.run()