from app import app
from db import *


@app.route('/')
@app.route('/index')
def index():
    a = Client("Emi")
    b = MockDatabase()
    b.createClient()
    print(list(map(lambda x: x.name(), b.clients())))
    return a.name()
