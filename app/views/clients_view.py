from app import response_renderer
from app.use_cases import *


def clients_index():
    data = get_clients()
    return response_renderer.successful_collection_response(data)


def clients_show(client_id):
    try:
        data = get_client(client_id)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def clients_create(name):
    try:
        new_client = create_client(name)
        return response_renderer.successful_object_response(new_client)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)


def clients_shop_queues(client_id):
    try:
        shop_queues = get_client_shop_queues(client_id)
        return response_renderer.successful_text_response(shop_queues)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def clients_let_through(client_id, queue_id):
    # responseText = MockDatabase.db.letThrough(client_id, queue_id)
    # if responseText != "OK":
    #     return response_renderer.bad_request_error_response(responseText)
    # else:
    #     return response_renderer.successful_text_response(responseText)
    return 0

