from app import app
from flask import request, jsonify, make_response
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





