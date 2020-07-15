import requests
from app.apis import api_formatter
from app import system_variables
from app import exceptions

BASE_URL = "http://noqueue789.herokuapp.com/api"
SYSTEM_ID_URI_PARAM = "system_id=" + str(system_variables.LOCAL_SYSTEM_ID)


def php_get_all_queues():
    resp = requests.get(BASE_URL + '/concepts?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return list(map(lambda q: api_formatter.DTOQueue.from_php_json(q), resp.json()))


def php_get_client_shop_queues(client_id):
    resp = requests.get(BASE_URL + '/users/' + str(client_id) + '/turns?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code >= 400:
        if "Not Found" in resp.text:
            return []
        else:
            raise exceptions.PhpApiError(resp.json())
    else:
        return list(
            map(lambda q:
                {
                    'id': q["concept_id"],
                    'name': 'PHP Queue',
                    'position': q["turn_order"],
                    'sourceId': system_variables.PHP_SYSTEM_ID
                },
                resp.json()
            )
        )


def php_enqueue_client(queue_id, client_id):
    body = {'concept_id': queue_id, 'user_id': client_id, 'name': "juan carlos", 'email': 'anemail@noemail.com'}
    resp = requests.post(BASE_URL + '/turns?' + SYSTEM_ID_URI_PARAM, data=body)
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return {'id': -1, 'clientId': -1, 'conceptQueueId': -1, 'state': "IN"}


# api_url/users/<client_id>/concepts/<concept_id>?system_id=<system_id>
def php_leave_queue(queue_id, client_id):
    resp = requests.delete(BASE_URL + '/users/' + str(client_id) + '/concepts/' + str(queue_id) + '?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return "Client removed from Queue"


# [POST]
# api_url/users/<client_id>/concepts/<concept_id>?system_id=<system_id>
# http://noqueue789.herokuapp.com/api/users/1/concepts/3?system_id=2
def php_let_through(queue_id, client_id):
    resp = requests.post(BASE_URL + '/users/' + str(client_id) + '/concepts/' + str(queue_id) + '?' + SYSTEM_ID_URI_PARAM)
    print(resp)
    print(resp.text)
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json()["error"])
    else:
        return "Client swapped"

# *
# 1- Todos los conceptos (api_url/queues?system_id=<system_id>) DONE
# 2- Turnos de un cliente (api_url/clients/<client_id>/shop_queues?system_id=<system_id>) DONE
# 3- Pedir un turno (api_url/queues/<queue_id>?client_id=<client_id>&system_id=<system_id>&source_id=<source_id>) DONE
# 4- Cancelar un turno/Irse de la cola (api_url/clients/<client_id>/leave_queue?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>&turn_id=<turn_id>) DONE
# (SOLO RAILS) 5- Confirmar un turno. DONE
# 6- Dejar pasar al siguiente (api_url/clients/<client_id>/let_through?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>&turn_id=<turn_id>)
# FALTA PHP CON EL TEMA DE QUE TIENE TANTO QUEUE_ID COMO CONCEPT_ID EN LET_THROUGH (DONE)

