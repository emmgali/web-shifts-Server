from app import app
from db import *
from app.views import *


MockDatabase()


@app.route('/')
@app.route('/index')
def index():
    a = Client("Emi")
    b = MockDatabase()
    b.createClient("Nacho2")
    print(list(map(lambda x: x.name(), b.clients())))
    return a.name()


@app.route('/tuvieja')
def tuvieja():
    MockDatabase.db.createClient("Nacho")
    print(list(map(lambda x: x.name(), MockDatabase.db.clients())))
    return "hola"
