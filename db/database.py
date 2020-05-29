# from app.models import *
# from app import exceptions
#
#
# class MockDatabase:
#     db = None
#
#     def __init__(self):
#         self._clients = []
#         self._owners = []
#         self._queues = []
#         MockDatabase.db = self
#
#     # GETTERS
#
#     def clients(self):
#         return self._clients
#
#     def owners(self):
#         return self._owners
#
#     def queues(self):
#         return self._queues
#
#     # DESTROY
#
#     def reset(self):
#         self._clients = []
#         self._owners = []
#         self._queues = []
#         return "The Database has been reset correctly"
#
#     # CLIENTS
#
#     def createClient(self, name=None):
#         if name is None:
#             raise exceptions.InvalidParameter("Name for Client must be present")
#         new_client = Client(name)
#         self._clients.append(new_client)
#         return new_client
#
#     def getClient(self, client_id):
#         searched_client = next((client for client in self._clients if client.id() == client_id), None)
#         if searched_client is None:
#             raise exceptions.NotFound("There is no client with that ID")
#         return searched_client
#
#     # OWNERS
#     def createOwner(self, name=None):
#         if name is None:
#             raise exceptions.InvalidParameter("Name for Owner must be present")
#         new_owner = Owner(name)
#         self._owners.append(new_owner)
#         return new_owner
#
#     def getOwner(self, owner_id):
#         searched_owner = next((owner for owner in self._owners if owner.id() == owner_id), None)
#         if searched_owner is None:
#             raise exceptions.NotFound("There is no owner with that ID")
#         return searched_owner
#
#     # QUEUES
#
#     def createQueue(self, name=None, capacity=None):
#         if name is None or capacity is None:
#             raise exceptions.InvalidParameter("Name and Capacity for Queue must be present")
#         new_queue = ConceptQueue(name, capacity)
#         self._queues.append(new_queue)
#         return new_queue
#
#     def getQueue(self, queue_id):
#         searched_queue = next((queue for queue in self._queues if queue.id() == queue_id), None)
#         if searched_queue is None:
#             raise exceptions.NotFound("There is no queue with that ID")
#         return searched_queue
#
#     def enqueue(self, queue_id, client_id):
#         searched_client = next((client for client in self._clients if client.id() == client_id), None)
#         searched_queue = next((queue for queue in self._queues if queue.id() == queue_id), None)
#         if searched_client is None or searched_queue is None:
#             return "ERROR DESPUES LO VEMOS"
#         searched_queue.enqueue(searched_client)
#         searched_client.enqueue(searched_queue)
#         return searched_client
#
#     def dequeue(self, queue_id):
#         searched_queue = next((queue for queue in self._queues if queue.id() == queue_id), None)
#         if searched_queue is None:
#             return "ERROR LO VEMOS DESPUES"
#         poped_client = searched_queue.dequeue(self.db)
#         return poped_client
#
#     def letThrough(self, client_id, queue_id):
#         searched_client = next((client for client in self._clients if client.id() == client_id), None)
#         searched_queue = next((queue for queue in self._queues if queue.id() == queue_id), None)
#         if searched_client is None or searched_queue is None:
#             return "ERROR DESPUES LO VEMOS"
#         #SI ESTOY SIENDO ATENTIDO -> NO PUEDO HACERLO. DECISION TOMADA POR EMI Y NACHO (26/5)
#         if searched_client.id() == searched_queue.actualClientId():
#             return "YA TE ESTAN ATENDIENDO"
#         else:
#             try:
#                 index = list(map(lambda client: client.id(), searched_queue.queue())).index(client_id)
#             except ValueError:
#                return "ERROR - NO ESTA EN LA LISTA"
#             if len(searched_queue.queue()) == index + 1:
#                 return "ERROR - NO HAY NADIE ATRAS DE EL"
#             else:
#                 queue = searched_queue.queue()
#                 queue[index+1], queue[index] = queue[index], queue[index+1] #SWAP PELELE
#                 return "OK"
#
#
#
#
