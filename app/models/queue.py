class Queue:
    class_counter = 0

    def __init__(self, id, name, capacity):
        self._id = Queue.class_counter + 1
        self._name = name
        self._capacity = capacity
        Queue.class_counter += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def capacity(self):
        return self._capacity
