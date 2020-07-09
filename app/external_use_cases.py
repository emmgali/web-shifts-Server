from app.models import *
from app import exceptions
from app.apis.rails_service import *
from app.use_cases import *
from app.apis.php_service import *

# ACÁ VAN LOS MÉTODOS PARA CUANDO A NUESTRA API LE PEGA ALGUIEN EXTERNO.


def external_get_all_queues():
    return get_all_local_queues()


def external_get_client_shop_queues(external_client_id, system_id):
    searched_client = get_client_by_external_id_and_source_id(external_client_id, system_id)
    return get_local_client_shop_queues(searched_client.id)


def external_enqueue_client(queue_id, client_id, system_id):
    try:
        searched_client = get_client_by_external_id_and_source_id(client_id, system_id)
        enqueue_client(queue_id, searched_client.id)
        queue = get_queue(queue_id)
        return {'position': queue.position(searched_client.id)}
    except exceptions.NotFound as e:
        searched_client = Client(externalId=client_id, sourceId=system_id)
        searched_client.create()
        enqueue_client(queue_id, searched_client.id)
        queue = get_queue(queue_id)
        return {'position': queue.position(searched_client.id)}


def external_leave_queue(queue_id, external_client_id, system_id):
    searched_client = get_client_by_external_id_and_source_id(external_client_id, system_id)
    searched_queue = get_queue(queue_id)
    removed_client_id = searched_queue.remove_client(searched_client.id)
    if removed_client_id is None:
        raise exceptions.InvalidParameter("There is no client in the queue")
    if len(searched_client.shopQueues) == 0:
        delete_client(searched_client.id)
    return "Client removed from Queue"


def external_let_through(external_client_id, queue_id, system_id):
    searched_client = get_client_by_external_id_and_source_id(external_client_id, system_id)
    local_let_through(searched_client.id, queue_id)
    return "Client swapped"

