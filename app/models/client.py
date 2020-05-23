from . import user as u


class Client(u.User):
    def __init__(self, name):
        super().__init__(name, "Client")
        self._shopQueues = []

    def shopQueues(self):
        return self._shopQueues

    def serialize(self):
        return {
            'id': self._id,
            'name': self._name,
            'type': self._type,
            'shop_queues': self._shopQueues
        }
