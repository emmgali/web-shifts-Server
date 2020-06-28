from app import response_renderer
from app.use_cases import *


def users_index(name, user_type):
    try:
        data = find_user_by(name, user_type)
        return response_renderer.successful_object_response(data)
    except exceptions.NotFound as e:
        return response_renderer.not_found_error_response(e.message)
    except exceptions.InvalidParameter as e:
        return response_renderer.bad_request_error_response(e.message)
