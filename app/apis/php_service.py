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
    # Probablemente necesitemos agregar un `turn_id` a esta respuesta dado que lo requerimos para el resto de
    # los endpoints de php tipo leave_queue y dejar pasar... O sea Grego se lo va a tener que guardar
    # así después nos lo pasa
    resp = requests.get(BASE_URL + '/users/' + str(client_id) + '/turns?' + SYSTEM_ID_URI_PARAM)
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return list(
            map(lambda q:
                {
                    'id': q["queue_id"],
                    'name': 'PHP Queue',
                    'position': q["turn_order"],
                    'system_id': system_variables.PHP_SYSTEM_ID
                },
                resp.json()
            )
        )


#201 RESPONSE:
#'{"email":"noemail@noemail.com","queue_id":"3","user_id":"2","turn_order":1,"turn_secret":"1eac1684-48c4-689e-9c65-6f32c4076e4e","updated_at":"2020-07-08T22:13:35.000000Z","created_at":"2020-07-08T22:13:35.000000Z","id":15}'
def php_enqueue_client(queue_id, client_id):
    body = {'queue_id': queue_id, 'user_id': client_id, 'email': 'noemail@noemail.com'}
    resp = requests.post(BASE_URL + '/turns?' + SYSTEM_ID_URI_PARAM, data=body)
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return {'id': -1, 'clientId': -1, 'conceptQueueId': -1, 'state': "IN"}


def php_leave_queue(client_id, queue_id):
    resp = requests.delete(BASE_URL + '/turns/' + str(client_id) + '/queue/' + str(queue_id) + '?' + SYSTEM_ID_URI_PARAM)
    # PROBLEMA, REQUIEREN EL TURN_ID Y NO LO TENEMOS, Y TAMPOCO TENDRÍAMOS QUE PERSISTIRLO.
    # Url posta: DELETE api/turns/{turn}
    # Invento que la Url es api/turns/{client_id}/queue/{queue_id}?system_id=2 para poder avanzar
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return "Client removed from Queue"


#POST api/concepts/{concept}/queues/{queue}/turns/{turn}
#PROBLEMA: requieren concept y turn que no tenemos, le mando queue_id siempre para poder avanzar
def php_let_through(client_id, queue_id):
    resp = requests.post(BASE_URL + '/concepts/' + str(queue_id) + '/queues/' + str(queue_id) + '/turns/' + str(queue_id))
    if resp.status_code >= 400:
        raise exceptions.PhpApiError(resp.json())
    else:
        return "Client swapped"

# *
# 1- Todos los conceptos (api_url/queues?system_id=<system_id>) DONE
# 2- Turnos de un cliente (api_url/clients/<client_id>/shop_queues?system_id=<system_id>) DONE
# 3- Pedir un turno (api_url/queues/<queue_id>?client_id=<client_id>&system_id=<system_id>&source_id=<source_id>) DONE
# 4- Cancelar un turno/Irse de la cola (api_url/clients/<client_id>/leave_queue?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
# EL 4 ESTÁ DONE EXCEPTO LO DEL TURN_ID DE PHP QUE NO LO TENEMOS POR AHORA, TENDRÍAMOS QUE MODIFICAR 2 Y 4 PARA MANDARLE AL FRONT
# EL TURN_ID CUANDO LE PEGAMOS A TURNOS DE PHP, Y QUE DESPUÉS EL FRONT NOS LO MANDE AL CANCELAR UN TURNO PARA QUE PODAMOS PEGARLE A PHP
# (SOLO RAILS) 5- Confirmar un turno.
# 6- Dejar pasar al siguiente (api_url/clients/<client_id>/let_through?queue_id=<queue_id>&system_id=<system_id>&source_id=<source_id>)
# FALTA PHP CON EL TURN_ID

