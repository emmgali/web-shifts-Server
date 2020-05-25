from app.models import *


class MockDatabase:
    db = None

    def __init__(self):
        self._clients = []
        self._owners = []
        self._queues = []
        MockDatabase.db = self

    # GETTERS

    def clients(self):
        return self._clients

    def owners(self):
        return self._owners

    def queues(self):
        return self._queues

    # CLIENTS

    def createClient(self, name):
        new_client = Client(name)
        self._clients.append(new_client)
        return new_client

    def getClient(self, client_id):
        searched_client = next(client for client in self._clients if client.id() == client_id)
        return searched_client

    # OWNERS
    def createOwner(self, name):
        new_owner = Owner(name)
        self._owners.append(new_owner)
        return new_owner

    def getOwner(self, owner_id):
        searched_owner = next(owner for owner in self._owners if owner.id() == owner_id)
        return searched_owner

    # QUEUES

    def createQueue(self, name, capacity):
        new_queue = ConceptQueue(name, capacity)
        self._queues.append(new_queue)
        return new_queue

    def getQueue(self, queue_id):
        searched_queue = next(queue for queue in self._queues if queue.id() == queue_id)
        return searched_queue

    def enqueue(self, queue_id, client_id):
        searched_client = next(client for client in self._clients if client.id() == client_id)
        searched_queue = next(queue for queue in self._queues if queue.id() == queue_id)
        searched_queue.enqueue(searched_client)
        searched_client.enqueue(searched_queue)
        return searched_client

    def dequeue(self, queue_id):
        searched_queue = next(queue for queue in self._queues if queue.id() == queue_id)
        poped_client = searched_queue.dequeue(self.db)
        return poped_client


