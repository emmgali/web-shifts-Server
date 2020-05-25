from . import user as u


class Client(u.User):
    def __init__(self, name):
        super().__init__(name, "Client")
        self._shopQueues = []

    def shopQueues(self):
        return self._shopQueues

    def enqueue(self, queue):
        self._shopQueues.append(queue)

    def removeFromShopQueue(self, queue_id):
        searched_queue = next(queue for queue in self._shopQueues if queue.id() == queue_id)
        self._shopQueues.remove(searched_queue)

    def showShopQueues(self):
        shopQueuesView = list(map(lambda q: { 'id': q.id(), 'name': q.name(), 'position': q.position(self._id) }, self._shopQueues))
        return shopQueuesView

    def serialize(self):
        return {
            'id': self._id,
            'name': self._name,
            'type': self._type,
            'shop_queues': list(map(lambda q: q.id(), self._shopQueues)),
        }
