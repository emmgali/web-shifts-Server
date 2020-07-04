import requests
from app.apis import api_formatter
from app import system_variables

BASE_URL = "http://noqueue789.herokuapp.com/api"
SYSTEM_ID_URI_PARAM = "system_id=" + system_variables.LOCAL_SYSTEM_ID


def php_get_all_queues():
    resp = requests.get(BASE_URL + '/concepts?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code != 200:
        #QUE EXPLOTE TODO
        return 0
    else:
        return list(map(lambda q: api_formatter.DTOQueue.from_php_json(q), resp.json()))







# *
# 1- Todos los conceptos (api_url/queues?system_id=<system_id>)
# 2- Turnos de un cliente (api_url/clients/<client_id>/shop_queues?system_id=<system_id>)
# 3- Pedir un turno (api_url/queues/<queue_id>?client_id=<client_id>&system_id=<system_id>&source_id=<source_id>)
# 4- Cancelar un turno/Irse de la cola (api_url/clients/<client_id>/leave_queue?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
# (SOLO RAILS) 5- Confirmar un turno
# 6- Dejar pasar al siguiente (api_url/clients/<client_id>/let_through?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
#

