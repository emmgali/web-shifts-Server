from flask import request
from app import routes, create_app, views
from db import MockDatabase

from flask_cors import CORS, cross_origin
app = create_app()
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


MockDatabase()

@app.route('/tuvieja')
def tuvieja():
    return "hola"


@app.route('/')
@app.route('/index')
def index():
    return routes.index()


# DATABASE
@app.route('/database/reset', methods=['POST'])
def database_reset():
    return views.database_reset()


# CLIENTS

@app.route('/clients', methods=['GET'])
def clients():
    return views.clients_index()


@app.route('/clients/<int:client_id>', methods=['GET'])
def clients_show(client_id):
    return views.clients_show(client_id)


@app.route('/clients', methods=['POST'])
def clients_create():
    return views.clients_create()


@app.route('/clients/<int:client_id>/shop_queues', methods=['GET'])
def clients_shop_queues(client_id):
    return views.clients_shop_queues(client_id)


@app.route('/clients/<int:client_id>/let_through', methods=['POST'])
def clients_let_through(client_id):
    queue_id = int(request.args["queue_id"])
    return views.clients_let_through(client_id, queue_id)


# OWNERS

@app.route('/owners', methods=['GET'])
def owners_index():
    return views.owners_index()


@app.route('/owners/<int:owner_id>', methods=['GET'])
def owners_show(owner_id):
    return owners_show(owner_id)


@app.route('/owners', methods=['POST'])
def owners_create():
    return owners_create()


# QUEUES
@app.route('/queues', methods=['GET'])
def queues_index():
    return views.queues_index()


@app.route('/queues/<int:queue_id>', methods=['GET'])
def queues_show(queue_id):
    return views.queues_show(queue_id)

@app.route('/queues', methods=['POST'])
def queues_create():
    return views.queues_create()

@app.route('/queues/<int:queue_id>', methods=['POST'])
def queues_enqueue_client(queue_id):
    client_id = int(request.args["client_id"])
    return views.queues_enqueue_client(queue_id, client_id)

@app.route('/queues/<int:queue_id>/serve_next', methods=['PUT'])
def queues_serve_next(queue_id):
    return views.queues_serve_next(queue_id)