from app.models import *
from app import exceptions
from app.apis.rails_service import *
from app.use_cases import *
from app.apis.php_service import *


def external_get_all_queues():
    rails_queues = rails_get_all_queues()
    local_queues = get_all_queues()
    php_queues = php_get_all_queues()

    return local_queues + rails_queues + php_queues

def external_clients_shop_queues(client_id):
    rails_shop_queues = rails_get_client_shop_queues(client_id)
    local_shop_queues = get_client_shop_queues(client_id)
    php_shop_queues = php_get_client_shop_queues(client_id)

    return local_shop_queues + rails_shop_queues + php_shop_queues

def enqueue_external_client(queue_id, client_id, system_id):
    try:
        searched_client = get_client_by_extrenalId_and_sourceId(client_id, system_id)
        return enqueue_client(queue_id, searched_client.id)
    except exceptions.NotFound as e:
        searched_client = Client(externalId=client_id, sourceId=system_id)
        searched_client.create()
        return enqueue_client(queue_id, searched_client.id)

