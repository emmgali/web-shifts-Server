from app.models import *
from app import exceptions


# OWNER USE CASES

def get_owners():
    return Owner.query.all()


def get_owner(owner_id):
    searched_owner = Owner.query.get(owner_id)
    if searched_owner is None:
        raise exceptions.NotFound("There is no owner with that ID")
    return searched_owner


def create_owner(name=None):
    if name is None:
        raise exceptions.InvalidParameter("Name for Owner must be present")
    new_owner = Owner(name=name)
    new_owner.create()
    return new_owner


# CLIENT USE CASES

def get_clients():
    return Client.query.all()


def get_client(client_id):
    searched_client = Client.query.get(client_id)
    if searched_client is None:
        raise exceptions.NotFound("There is no client with that ID")
    return searched_client


def create_client(name=None):
    if name is None:
        raise exceptions.InvalidParameter("Name for Client must be present")
    new_client = Client(name=name)
    new_client.create()
    return new_client


def get_client_shop_queues(client_id):
    searched_client = get_client(client_id)
    # agregar position del cliente en la shopQueue!
    return list(map(lambda q: { 'id': q.id, 'name': q.name }, searched_client.shopQueues))

# FALTA LET_THROUGH DE CLIENTS


# QUEUES USE CASES
