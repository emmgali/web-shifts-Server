from . import user as u


class Owner(u.User):
    def __init__(self, name):
        super().__init__(name, "Owner"),
        self._ownedQueues = []

    def ownedQueues(self):
        return self._ownedQueues

    def serialize(self):
        return {
            'id': self._id,
            'name': self._name,
            'type': self._type,
            'owned_queues': self._ownedQueues
        }