from flask import request
from db import *

from app import response_renderer, create_app
from app import exceptions


def owners_index():
    data = MockDatabase.db.owners()
    return response_renderer.successful_collection_response(data)


def owners_show(owner_id):
    try:
        data = MockDatabase.db.getOwner(owner_id)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def owners_create():
    data = request.form
    name = data.get("name")
    try:
        new_owner = MockDatabase.db.createOwner(name)
        return response_renderer.successful_object_response(new_owner)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
