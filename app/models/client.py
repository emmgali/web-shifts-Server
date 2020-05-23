from . import user as u


class Client(u.User):
    def __init__(self, name):
        super().__init__(name, "Client")
        self._shopQueues = []

    def shopQueues(self):
        return self._shopQueues
