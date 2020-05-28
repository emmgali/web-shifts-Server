from app import app
from flask import request
from db import *

from app import response_renderer
from app import exceptions


@app.route('/queues', methods=['GET'])
def queues_index():
    data = MockDatabase.db.queues()
    return response_renderer.successful_collection_response(data)


@app.route('/queues/<int:queue_id>', methods=['GET'])
def queues_show(queue_id):
    try:
        data = MockDatabase.db.getQueue(queue_id)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


@app.route('/queues', methods=['POST'])
def queues_create():
    data = request.form
    name = data.get("name")
    capacity = data.get("capacity")
    try:
        new_queue = MockDatabase.db.createQueue(name, capacity)
        return response_renderer.successful_object_response(new_queue)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)


@app.route('/queues/<int:queue_id>', methods=['POST'])
def queues_enqueue_client(queue_id):
    client_id = int(request.args["client_id"])
    enqueued_client = MockDatabase.db.enqueue(queue_id, client_id)
    return response_renderer.successful_object_response(enqueued_client)


@app.route('/queues/<int:queue_id>/serve_next', methods=['PUT'])
def queues_serve_next(queue_id):
    poped_client = MockDatabase.db.dequeue(queue_id)
    if poped_client == 0:
        data = []
    else:
        data = poped_client.serialize()
    return response_renderer.successful_text_response(data)