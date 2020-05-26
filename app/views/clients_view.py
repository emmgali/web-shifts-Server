from app import app
from flask import request, jsonify, make_response
from flask_api import status

from db import *
import json


@app.route('/clients', methods=['GET'])
def clients_index():
    data = list(map(lambda x: x.serialize(), MockDatabase.db.clients()))
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/clients/<int:client_id>', methods=['GET'])
def clients_show(client_id):
    data = MockDatabase.db.getClient(client_id).serialize()
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/clients', methods=['POST'])
def clients_create():
    data = request.form
    name = data["name"]
    new_client = MockDatabase.db.createClient(name)
    response = make_response(json.dumps(new_client.serialize()))
    response.mimetype = 'application/json'
    return response


@app.route('/clients/<int:client_id>/shop_queues', methods=['GET'])
def clients_shop_queues(client_id):
    searched_client = MockDatabase.db.getClient(client_id)
    shopQueuesVista = searched_client.showShopQueues()
    response = make_response(json.dumps(shopQueuesVista))
    response.mimetype = 'application/json'
    return response


#PARAMETROS POR URI???
@app.route('/clients/<int:client_id>/<int:queue_id>/let_through', methods=['POST'])
def clients_let_through(client_id, queue_id):
    responseText = MockDatabase.db.letThrough(client_id, queue_id)
    if responseText is not "OK":
        statusCode = status.HTTP_404_NOT_FOUND
    else:
        statusCode = status.HTTP_200_OK
    response = make_response(responseText)
    response.mimetype = 'application/json'
    return response, statusCode



