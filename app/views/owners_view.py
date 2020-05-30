from app import response_renderer
from app.use_cases import *


def owners_index():
    data = get_owners()
    return response_renderer.successful_collection_response(data)


def owners_show(owner_id):
    try:
        data = get_owner(owner_id)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def owners_create(name):
    try:
        new_owner = create_owner(name)
        return response_renderer.successful_object_response(new_owner)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
