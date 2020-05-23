from app.models import *


class MockDatabase:
    db = None

    def __init__(self):
        self._clients = []
        self._owners = []
        self._queues = []
        MockDatabase.db = self

    def clients(self):
        return self._clients

    def owners(self):
        return self._owners

    def queues(self):
        return self._queues

    def createClient(self):
        self._clients.append(Client("Carlos"))
