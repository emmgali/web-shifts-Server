import requests
from app.apis import api_formatter
from app import system_variables
from app import exceptions

BASE_URL = "https://the-queue-arq-web.herokuapp.com/api"
SYSTEM_ID_URI_PARAM = "sistema_id=" + str(system_variables.LOCAL_SYSTEM_ID)


def rails_get_all_queues():
    resp = requests.get(BASE_URL + '/conceptos?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code >= 400:
        raise exceptions.RailsApiError(resp.json()["mensaje"])
    else:
        return list(map(lambda q: api_formatter.DTOQueue.from_rails_json(q), resp.json()["concepto"]))


def rails_get_client_shop_queues(client_id):
    resp = requests.get(BASE_URL + '/clientes/turnos?cliente_id=' + str(client_id) + '&' + SYSTEM_ID_URI_PARAM)
    if resp.status_code >= 400:
        raise exceptions.RailsApiError(resp.json()["mensaje"])
    else:
        return list(
            map(lambda q:
                {
                    'id': q["concepto_id"],
                    'name': 'Ruby Queue',
                    'position': q["orden"],
                    'system_id': system_variables.RAILS_SYSTEM_ID
                },
                resp.json()["turnos"]
            )
        )


def rails_enqueue_client(queue_id,client_id):
    resp = requests.get(BASE_URL + '/clientes/pedir_turno?cliente_id=' + str(client_id) + '&' + SYSTEM_ID_URI_PARAM + '&concepto_id=' + str(queue_id))
    response_message = resp.json()["mensaje"]
    if resp.status_code >= 400:
        raise exceptions.RailsApiError(response_message)
    else:
        if response_message[:2] == "Ya" or response_message[:2] == "Lo":
            raise exceptions.RailsApiError(response_message)
        else:
            return {'id': -1, 'clientId': -1, 'conceptQueueId': -1, 'state': "IN", 'turnId': 0}


def rails_leave_queue(client_id, queue_id):
    resp = requests.get(BASE_URL + '/clientes/cancelar_turno?cliente_id=' + str(client_id) + '&' + SYSTEM_ID_URI_PARAM + '&concepto_id=' + str(queue_id))
    response_message = resp.json()["mensaje"]
    if resp.status_code >= 400:
        raise exceptions.RailsApiError(response_message)
    else:
        if response_message[:2] == "No":
            raise exceptions.RailsApiError(response_message)
        else:
            return "Client removed from Queue"


def rails_confirm_turn(client_id, queue_id):
    resp = requests.get(BASE_URL + '/clientes/confirmar_turno?cliente_id=' + str(client_id) + '&' + SYSTEM_ID_URI_PARAM + '&concepto_id=' + str(queue_id))
    response_message = resp.json()["mensaje"]
    if resp.status_code >= 400:
        raise exceptions.RailsApiError(response_message)
    else:
        if response_message[:2] == "No" or response_message[:2] == "Lo":
            raise exceptions.RailsApiError(response_message)
        else:
            return "Client confirmed in Queue"


def rails_let_through(client_id, queue_id):
    resp = requests.get(BASE_URL + '/clientes/saltear_turno?cliente_id=' + str(client_id) + '&' + SYSTEM_ID_URI_PARAM + '&concepto_id=' + str(queue_id))
    response_message = resp.json()["mensaje"]
    if resp.status_code >= 400:
        raise exceptions.RailsApiError(response_message)
    else:
        if response_message[:2] == "So":
            raise exceptions.RailsApiError(response_message)
        else:
            return "Client swapped"

# *
# 1- Todos los conceptos (api_url/queues?system_id=<system_id>) DONE
# 2- Turnos de un cliente (api_url/clients/<client_id>/shop_queues?system_id=<system_id>) DONE
# 3- Pedir un turno (api_url/queues/<queue_id>?client_id=<client_id>&system_id=<system_id>&source_id=<source_id>) DONE
# 4- Cancelar un turno/Irse de la cola (api_url/clients/<client_id>/leave_queue?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>) DONE
# (SOLO RAILS) 5- Confirmar un turno. DONE
# 6- Dejar pasar al siguiente (api_url/clients/<client_id>/let_through?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
# FALTA PHP CON EL TEMA DE QUE TIENE TANTO QUEUE_ID COMO CONCEPT_ID EN LET_THROUGH

