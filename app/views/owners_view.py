from app import app
from flask import request
from db import *

from app import response_renderer


@app.route('/owners', methods=['GET'])
def owners_index():
    data = MockDatabase.db.owners()
    return response_renderer.successful_collection_response(data)


@app.route('/owners/<int:owner_id>', methods=['GET'])
def owners_show(owner_id):
    data = MockDatabase.db.getOwner(owner_id)
    return response_renderer.successful_object_response(data)


@app.route('/owners', methods=['POST'])
def owners_create():
    data = request.form
    name = data["name"]
    new_owner = MockDatabase.db.createOwner(name)
    return response_renderer.successful_object_response(new_owner)
