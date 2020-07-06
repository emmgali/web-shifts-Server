from app.models import *
from app import exceptions
import app.apis.rails_service
import app.apis.php_service


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
    if User.filter_by(name):
        raise exceptions.InvalidParameter("An User with that name already exists")
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


def get_client_by_external_id_and_source_id(external_client_id, system_id):
    searched_client = Client.query.filter_by(externalId=external_client_id, sourceId=system_id).first()
    if searched_client is None:
        raise exceptions.NotFound("There is no client with that ID")
    return searched_client


def create_client(name=None):
    if name is None:
        raise exceptions.InvalidParameter("Name for Client must be present")
    if User.filter_by(name):
        raise exceptions.InvalidParameter("An User with that name already exists")
    new_client = Client(name=name)
    new_client.create()
    new_client.setExternalParameters(new_client.id, system_variables.LOCAL_SYSTEM_ID)

    return new_client


def get_client_shop_queues(client_id):
    rails_shop_queues = app.apis.rails_service.rails_get_client_shop_queues(client_id)
    local_shop_queues = get_local_client_shop_queues(client_id)
    php_shop_queues = app.apis.php_service.php_get_client_shop_queues(client_id)

    return local_shop_queues + rails_shop_queues + php_shop_queues


def get_local_client_shop_queues(client_id):
    searched_client = get_client(client_id)
    return list(
        map(lambda q: {'id': q.id, 'name': q.name, 'position': q.position(client_id)}, searched_client.all_queues()))


def leave_queue(client_id, queue_id, source_id):
    if source_id == system_variables.RAILS_SYSTEM_ID:
        return app.apis.rails_service.rails_leave_queue(client_id, queue_id)
    elif source_id == system_variables.PHP_SYSTEM_ID:
        return app.apis.php_service.php_leave_queue(client_id, queue_id)
    else:
        return local_leave_queue(client_id, queue_id)


def local_leave_queue(client_id, queue_id):
    get_client(client_id)  # for raising exception if client did not exist
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


def delete_client(client_id):
    client_to_delete = get_client(client_id)
    client_to_delete.delete()
    return


def confirm_turn(client_id=None, queue_id=None):
    if client_id is None:
        raise exceptions.InvalidParameter("Client id must be present")
    if queue_id is None:
        raise exceptions.InvalidParameter("Rails Queue id must be present")
    get_client(client_id)
    return app.apis.rails_service.rails_confirm_turn(client_id, queue_id)


# USER USE CASES

def find_user_by(name=None, user_type=None):
    if name is None:
        raise exceptions.InvalidParameter("Name for User must be present")
    if user_type is None:
        raise exceptions.InvalidParameter("You must indicate if you are a Client or an Owner")
    users_found = User.filter_by(name, user_type)
    if not users_found:
        raise exceptions.NotFound("There's no User matching the criteria")
    return users_found[0]


# QUEUES USE CASES

def get_all_queues():
    rails_queues = app.apis.rails_service.rails_get_all_queues()
    local_queues = get_all_local_queues()
    php_queues = app.apis.php_service.php_get_all_queues()

    return local_queues + rails_queues + php_queues


def get_all_local_queues():
    return ConceptQueue.query.all()


def get_queue(queue_id):
    searched_queue = ConceptQueue.query.get(queue_id)
    if searched_queue is None:
        raise exceptions.NotFound("There is no queue with that ID")
    return searched_queue


def create_queue(name=None, description=None, owner_id=None, capacity=0, longitude=0, latitude=0):
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

    try:
        float(longitude)
    except ValueError:
        raise exceptions.InvalidParameter("Longitude is not a valid number")

    try:
        float(latitude)
    except ValueError:
        raise exceptions.InvalidParameter("Latitude is not a valid number")

    new_queue = ConceptQueue(name=name, description=description, ownerId=owner_id, capacity=capacity,
                             longitude=longitude, latitude=latitude)
    new_queue.create()
    return new_queue


def enqueue_client(queue_id, client_id):
    get_client(client_id)     # For raising exception if client does not exist
    searched_queue = get_queue(queue_id)
    if searched_queue.has_client(client_id):
        raise exceptions.InvalidParameter("Client already in queue")
    if searched_queue.is_full():
        raise exceptions.InvalidParameter("Queue is full")
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
