#Guðmundur Jóns
from bottle import route, run, template

@route('/')
def index():
    return \
        "<a href='/about'>About </a> <br>" \
        " <a href='/bio'>Bio </a> <br>" \
        " <a href='/pic'>Pictures</a>"

@route('/about')
def about():
    return "upplýsingar um Steve Jobs: hann var hippi"

@route('/bio')
def bio():
    return "Biography, Steve Jobs"

@route('/pic')
def pic():
    return "Hérna er mynd af Steve Jobs"


run(host='localhost', port=8080)
