import requests
from app.apis import api_formatter
from app import system_variables

BASE_URL = "https://the-queue-arq-web.herokuapp.com/api"
SYSTEM_ID_URI_PARAM = "system_id=" + str(system_variables.LOCAL_SYSTEM_ID)


def rails_get_all_queues():
    resp = requests.get(BASE_URL + '/conceptos?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code != 200:
        #QUE EXPLOTE TODO
        return 0
    else:
        return list(map(lambda q: api_formatter.DTOQueue.from_rails_json(q), resp.json()["concepto"]))


def rails_get_client_shop_queues(client_id):
    resp = requests.get(BASE_URL + '/clientes/' + client_id + '?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code != 200:
        #QUE EXPLOTE TODO
        return 0
    else:
        return list(
            map(lambda q:
                {'id': q.Concept_id, 'name': 'Ruby Queue', 'position': q.Orden, 'system_id': system_variables.RAILS_SYSTEM_ID},
                resp.json()["Turnos"]))

def rails_enqueue_client(queue_id,client_id):
    resp = requests.get(BASE_URL + '/clientes/' + client_id + '/conceptos/' + queue_id + '/pedir_turno?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code != 200:
        #QUE EXPLOTE TODO
        return 0
    else:
        return {'id': -1, 'clientId': -1, 'conceptQueueId': -1, 'state': "IN"}


# *
# 1- Todos los conceptos (api_url/queues?system_id=<system_id>) DONE
# 2- Turnos de un cliente (api_url/clients/<client_id>/shop_queues?system_id=<system_id>) DONE
# 3- Pedir un turno (api_url/queues/<queue_id>?client_id=<client_id>&system_id=<system_id>&source_id=<source_id>) DONE
# 4- Cancelar un turno/Irse de la cola (api_url/clients/<client_id>/leave_queue?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
# (SOLO RAILS) 5- Confirmar un turno
# 6- Dejar pasar al siguiente (api_url/clients/<client_id>/let_through?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
#

