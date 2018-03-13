from src.bottle import Bottle, run, view

app = Bottle()


@app.route('/')
@view('template.tpl')
def hello():
    context = {'title': "Bienvenue sur l'API"}
    return context


run(app, host='localhost', port=5200)