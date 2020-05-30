from flask import request
from app import routes, create_app, views
from db import MockDatabase

from flask_cors import CORS, cross_origin
app = create_app()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


MockDatabase()

@app.route('/tuvieja')
@cross_origin()
def tuvieja():
    return "hola"


@app.route('/')
@app.route('/index')
@cross_origin()
def index():
    return routes.index()


# DATABASE
@app.route('/database/reset', methods=['POST'])
@cross_origin()
def database_reset():
    return views.database_reset()


# CLIENTS

@app.route('/clients', methods=['GET'])
@cross_origin()
def clients():
    return views.clients_index()


@app.route('/clients/<int:client_id>', methods=['GET'])
@cross_origin()
def clients_show(client_id):
    return views.clients_show(client_id)


@app.route('/clients', methods=['POST'])
@cross_origin()
def clients_create():
    return views.clients_create()


@app.route('/clients/<int:client_id>/shop_queues', methods=['GET'])
@cross_origin()
def clients_shop_queues(client_id):
    return views.clients_shop_queues(client_id)


@app.route('/clients/<int:client_id>/let_through', methods=['POST'])
@cross_origin()
def clients_let_through(client_id):
    queue_id = int(request.args["queue_id"])
    return views.clients_let_through(client_id, queue_id)


# OWNERS

@app.route('/owners', methods=['GET'])
@cross_origin()
def owners_index():
    return views.owners_index()


@app.route('/owners/<int:owner_id>', methods=['GET'])
@cross_origin()
def owners_show(owner_id):
    return owners_show(owner_id)


@app.route('/owners', methods=['POST'])
@cross_origin()
def owners_create():
    return owners_create()


# QUEUES
@app.route('/queues', methods=['GET'])
@cross_origin()
def queues_index():
    return views.queues_index()


@app.route('/queues/<int:queue_id>', methods=['GET'])
@cross_origin()
def queues_show(queue_id):
    return views.queues_show(queue_id)

@app.route('/queues', methods=['POST'])
@cross_origin()
def queues_create():
    return views.queues_create()

@app.route('/queues/<int:queue_id>', methods=['POST'])
@cross_origin()
def queues_enqueue_client(queue_id):
    client_id = int(request.args["client_id"])
    return views.queues_enqueue_client(queue_id, client_id)

@app.route('/queues/<int:queue_id>/serve_next', methods=['PUT'])
@cross_origin()
def queues_serve_next(queue_id):
    return views.queues_serve_next(queue_id)