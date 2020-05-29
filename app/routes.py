#from app import app
from db import *
from app.views import *


MockDatabase()

def index():
    a = Client("Emi")
    b = MockDatabase()
    b.createClient("Nacho2")
    print(list(map(lambda x: x.name(), b.clients())))
    return a.name()

