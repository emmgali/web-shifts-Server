from app import app
from .models import user as u
from .models import client as c
from .models import owner as o
from .models import queue as q


@app.route('/')
@app.route('/index')
def index():
    a = c.Client("Emi")
    return a.name()
