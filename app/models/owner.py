from . import user as u


class Owner(u.User):
    def __init__(self, name):
        super().__init__(name, "Owner"),
        self._ownedQueues = []

    def ownedQueues(self):
        return self._ownedQueues
