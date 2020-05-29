from app import response_renderer, create_app

# from db import *


def database_reset():
    data = MockDatabase.db.reset()
    return response_renderer.successful_text_response(data)
