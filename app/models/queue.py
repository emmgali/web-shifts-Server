import pickle


class Queue:
    class_counter = 0

    def __init__(self, name, capacity):
        self._id = Queue.class_counter + 1
        self._name = name
        self._capacity = capacity
        self._queue = []
        Queue.class_counter += 1

    # GETTERS

    def id(self):
        return self._id

    def name(self):
        return self._name

    def capacity(self):
        return self._capacity

    def queue(self):
        return self._queue

    # OTHER

    def next(self):
        return self._queue.first

    def enqueue(self, client):
        self._queue.append(client)

    def dequeue(self):
        return self._queue.pop()

    def serialize(self):
        return {
            'id': self._id,
            'name': self._name,
            'capacity': self._capacity,
            #'queue': self._queue <--- Si descomentas esto explota el programa. No podemos serializar listas
        }
