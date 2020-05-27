from app import app
from flask import request
from app import response_renderer

from db import *
from app import exceptions


@app.route('/clients', methods=['GET'])
def clients_index():
    data = MockDatabase.db.clients()
    return response_renderer.successful_collection_response(data)


@app.route('/clients/<int:client_id>', methods=['GET'])
def clients_show(client_id):
    try:
        data = MockDatabase.db.getClient(client_id)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


@app.route('/clients', methods=['POST'])
def clients_create():
    data = request.form
    name = data["name"]
    new_client = MockDatabase.db.createClient(name)
    return response_renderer.successful_object_response(new_client)


@app.route('/clients/<int:client_id>/shop_queues', methods=['GET'])
def clients_shop_queues(client_id):
    searched_client = MockDatabase.db.getClient(client_id)
    shopQueuesVista = searched_client.showShopQueues()
    return response_renderer.successful_text_response(shopQueuesVista)


#PARAMETROS POR URI???
@app.route('/clients/<int:client_id>/<int:queue_id>/let_through', methods=['POST'])
def clients_let_through(client_id, queue_id):
    responseText = MockDatabase.db.letThrough(client_id, queue_id)
    if responseText is not "OK":
        return response_renderer.bad_request_error_response(responseText)
    else:
        return response_renderer.successful_text_response(responseText)




