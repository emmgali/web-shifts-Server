from app import exceptions
from app import response_renderer

@app.errorhandler(exceptions.NotFound)
def handle_not_found(e):
    return response_renderer.not_found_error_response(e.message)