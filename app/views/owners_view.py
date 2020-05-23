from app import app
from flask import request, jsonify, make_response
from db import *
import json


@app.route('/owners', methods=['GET'])
def owners_index():
    return "grego gato"


@app.route('/owners/<int:owner_id>', methods=['GET'])
def owners_show(owner_id):
    return "grego gato"


@app.route('/owners', methods=['POST'])
def owners_create():
    return "grego gato"
