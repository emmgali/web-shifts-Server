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
    return list(
        map(lambda q: {'id': q.id, 'name': q.name, 'position': q.position(client_id)}, searched_client.shopQueues))


def leave_queue(client_id, queue_id):
    get_client(client_id)       # for raising exception if client did not exist
    searched_queue = get_queue(queue_id)
    removed_client_id = searched_queue.remove_client(client_id)
    if removed_client_id is None:
        raise exceptions.InvalidParameter("There is no client in the queue")
    return "Client removed from Queue"


def let_through(client_id, queue_id):
    get_client(client_id)   # for raising exception if client did not exist
    searched_queue = get_queue(queue_id)
    if not searched_queue.has_client(client_id):
        raise exceptions.InvalidParameter("There is no client in the queue")
    if searched_queue.actualClientId == client_id:
        raise exceptions.InvalidParameter("You can't let through when you are the actual client")
    if not searched_queue.are_clients_behind(client_id):
        raise exceptions.InvalidParameter("There is no one left")
    searched_queue.swap_client(client_id)
    return "Client swapped"


# QUEUES USE CASES

def get_all_queues():
    return ConceptQueue.query.all()


def get_queue(queue_id):
    searched_queue = ConceptQueue.query.get(queue_id)
    if searched_queue is None:
        raise exceptions.NotFound("There is no queue with that ID")
    return searched_queue


def create_queue(name=None, owner_id=None, capacity=0, longitude=0, latitude=0):
    if name is None:
        raise exceptions.InvalidParameter("Name for Queue must be present")
    if owner_id is None:
        raise exceptions.InvalidParameter("Owner for Queue must be present")
    if Owner.query.get(owner_id) is None:
        raise exceptions.InvalidParameter("Owner does not exist")
    if longitude is None:
        raise exceptions.InvalidParameter("Longitude is not a valid number")
    if latitude is None:
        raise exceptions.InvalidParameter("Latitude is not a valid number")

    new_queue = ConceptQueue(name=name, ownerId=owner_id, capacity=capacity, longitude=longitude, latitude=latitude)
    new_queue.create()
    return new_queue


def enqueue_client(queue_id, client_id):
    get_client(client_id)     # For raising exception if client does not exist
    searched_queue = get_queue(queue_id)
    if searched_queue.has_client(client_id):
        raise exceptions.InvalidParameter("Client already in queue")

    new_entry = ConceptQueueEntry(clientId=client_id, conceptQueueId=queue_id, state="IN")
    new_entry.create()
    return new_entry


def serve_next(queue_id):
    searched_queue = get_queue(queue_id)
    if searched_queue is None:
        raise exceptions.InvalidParameter("Queue does not exist")
    attended_client_id = searched_queue.dequeue_and_attend()
    if attended_client_id is None:
        return None
    else:
        return get_client(attended_client_id)


def delete_queue(queue_id):
    searched_queue = get_queue(queue_id)
    response_text = searched_queue.delete()
    return response_text


def show_entries(queue_id):
    searched_queue = get_queue(queue_id)
    if searched_queue is None:
        raise exceptions.InvalidParameter("Queue does not exist")
    return searched_queue.entries
