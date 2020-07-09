from app import response_renderer
from app.use_cases import *
from app.external_use_cases import *


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


def clients_shop_queues(client_id, system_id):
    try:
        if system_id == system_variables.LOCAL_SYSTEM_ID:
            shop_queues = get_client_shop_queues(client_id)
        else:
            shop_queues = external_get_client_shop_queues(client_id, system_id)
        return response_renderer.successful_text_response(shop_queues)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)
    except exceptions.RailsApiError as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.PhpApiError as e:
        return response_renderer.bad_request_error_response(e.message)


def clients_let_through(client_id, queue_id, system_id, source_id):
    try:
        if system_id == system_variables.LOCAL_SYSTEM_ID:
            response_text = let_through(client_id, queue_id, source_id)
        else:
            response_text = external_let_through(client_id, queue_id, system_id)
        return response_renderer.successful_text_response(response_text)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)
    except exceptions.RailsApiError as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.PhpApiError as e:
        return response_renderer.bad_request_error_response(e.message)


def clients_leave_queue(client_id, queue_id, system_id, source_id):
    try:
        if system_id == system_variables.LOCAL_SYSTEM_ID:
            response_text = leave_queue(client_id, queue_id, source_id)
        else:
            response_text = external_leave_queue(queue_id, client_id, system_id)
        return response_renderer.successful_text_response(response_text)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)
    except exceptions.RailsApiError as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.PhpApiError as e:
        return response_renderer.bad_request_error_response(e.message)


def clients_confirm_turn(client_id, rails_queue_id):
    try:
        response_text = confirm_turn(client_id, rails_queue_id)
        return response_renderer.successful_text_response(response_text)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.RailsApiError as e:
        return response_renderer.bad_request_error_response(e.message)
