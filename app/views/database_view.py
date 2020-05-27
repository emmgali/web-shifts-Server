from app import app
from app import response_renderer

from db import *


@app.route('/database/reset', methods=['POST'])
def database_reset():
    data = MockDatabase.db.reset()
    return response_renderer.successful_text_response(data)
