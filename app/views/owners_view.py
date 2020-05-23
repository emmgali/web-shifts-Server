from app import app
from flask import request, jsonify, make_response
from db import *
import json


@app.route('/owners', methods=['GET'])
def owners_index():
    data = list(map(lambda x: x.serialize(), MockDatabase.db.owners()))
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/owners/<int:owner_id>', methods=['GET'])
def owners_show(owner_id):
    data = MockDatabase.db.getOwner(owner_id).serialize()
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    return response


@app.route('/owners', methods=['POST'])
def owners_create():
    data = request.form
    name = data["name"]
    new_owner = MockDatabase.db.createOwner(name)

    return json.dumps(new_owner.serialize())
