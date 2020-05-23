from models import *


class MockDatabase:
    def __init__(self):
        self._clients = []
        self._owners = []
        self._queues = []

    def clients(self):
        return self._clients

    def owners(self):
        return self._owners

    def queues(self):
        return self._queues

    def createClient(self):
        self._clients.append(Client("Carlos"))
