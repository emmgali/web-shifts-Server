from app import app
from flask import request, jsonify, make_response
from db import *
import json


@app.route('/queues', methods=['GET'])
def queues_index():
    data = list(map(lambda x: x.serialize(), MockDatabase.db.queues()))
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/queues/<int:queue_id>', methods=['GET'])
def queues_show(queue_id):
    data = MockDatabase.db.getQueue(queue_id).serialize()
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/queues', methods=['POST'])
def queues_create():
    data = request.form
    name = data["name"]
    capacity = data["capacity"]
    new_queue = MockDatabase.db.createQueue(name, capacity)

    return json.dumps(new_queue.serialize())


@app.route('/queues/<int:queue_id>', methods=['POST'])
def queues_enqueue_client(queue_id):
    client_id = int(request.args["client_id"])
    enqueued_client = MockDatabase.db.enqueue(queue_id, client_id)
    # Object of type Client is not JSON serializable

    response = make_response(json.dumps(enqueued_client.serialize()))
    response.mimetype = 'application/json'
    return response

