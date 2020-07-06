from app.models import *
from app import exceptions
from app.apis.rails_service import *
from app.use_cases import *
from app.apis.php_service import *


# EMI Y NACHO LEER ESTO
# ACÁ VAN LOS MÉTODOS PARA CUANDO A NUESTRA API LE PEGA ALGUIEN EXTERNO.
# Hoy 6/7 me di cuenta que para get_all_queues y client_shop_queues pusimos acá los métodos para cuando Grego nos pega
# Pero para enqueue_client y client_leave_queue pusimos acá los métodos para cuando nos pega alguien externo.
# Así que refactoricé y puse acá los endpoints para cuando a nuestra api le pega alguien externo
# Pueden fichar cómo estaba el código previo al commit en el que refactorizo

# Si quieren refactorizar y que sea al revés estoy de acuerdo también (o sea que acá vayan los endpoints
# para cuando nos pega Grego), siempre y cuando seamos correlativos con nuestra implementación y no mezclemos.

# Por mí borren estos comments de arriba cuando lo lean, si pueden dejar sólo la decisión final va mejor jaja


def external_get_all_queues():
    return get_all_local_queues()


def external_get_client_shop_queues(external_client_id, system_id):
    searched_client = get_client_by_external_id_and_source_id(external_client_id, system_id)
    return get_local_client_shop_queues(searched_client.id)


def enqueue_external_client(queue_id, client_id, system_id):
    try:
        searched_client = get_client_by_external_id_and_source_id(client_id, system_id)
        return enqueue_client(queue_id, searched_client.id)
    except exceptions.NotFound as e:
        searched_client = Client(externalId=client_id, sourceId=system_id)
        searched_client.create()
        return enqueue_client(queue_id, searched_client.id)


def external_leave_queue(queue_id, external_client_id, system_id):
    searched_client = get_client_by_external_id_and_source_id(external_client_id, system_id)
    searched_queue = get_queue(queue_id)
    removed_client_id = searched_queue.remove_client(searched_client.id)
    if removed_client_id is None:
        raise exceptions.InvalidParameter("There is no client in the queue")
    if len(searched_client.shopQueues) == 0:
        delete_client(searched_client.id)
    return {'message': "Client removed from Queue"}
