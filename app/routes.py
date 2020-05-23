from app import app
from db import *


MockDatabase()


@app.route('/')
@app.route('/index')
def index():
    a = Client("Emi")
    b = MockDatabase()
    b.createClient()
    print(list(map(lambda x: x.name(), b.clients())))
    return a.name()


@app.route('/tuvieja', viewsPackage.client.tuVieja(e))
def tuvieja():
    MockDatabase.db.createClient()
    print(list(map(lambda x: x.name(), MockDatabase.db.clients())))
    return "hola"
