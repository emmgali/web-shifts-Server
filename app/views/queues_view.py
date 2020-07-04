from app import response_renderer
from app.use_cases import *
from app.external_use_cases import *
from app.system_variables import *


def queues_index(system_id):
    if system_id == system_variables.LOCAL_SYSTEM_ID:
        data = get_all_queues()
    else:
        data = external_get_all_queues()
    return response_renderer.successful_collection_response(data)


def queues_show(queue_id):
    try:
        data = get_queue(queue_id)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def queues_create(name, description, capacity, owner_id, longitude, latitude):
    try:
        new_queue = create_queue(name, description, owner_id, capacity, longitude, latitude)
        return response_renderer.successful_object_response(new_queue)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)


def queues_enqueue_client(queue_id, client_id):
    try:
        concept_queue_entry = enqueue_client(queue_id, client_id)
        return response_renderer.successful_object_response(concept_queue_entry)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def queues_serve_next(queue_id):
    try:
        attended_client = serve_next(queue_id)
        return response_renderer.successful_object_response(attended_client)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)


def queues_delete(queue_id):
    try:
        response_text = delete_queue(queue_id)
        return response_renderer.successful_text_response(response_text)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)


def queues_get_entries(queue_id):
    try:
        entries = show_entries(queue_id)
        return response_renderer.successful_collection_response(entries)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)