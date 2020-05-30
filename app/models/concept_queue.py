from wsgi import db


class ConceptQueue(db.Model):
    __tablename__ = 'concept_queues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    capacity = db.Column(db.Integer)
    latitude = db.Column(db.Numeric(10, 3))
    longitude = db.Column(db.Numeric(10, 3))
    actualClient = db.Column(db.Integer, db.ForeignKey('clients.id'))
    ownerId = db.Column(db.Integer, db.ForeignKey('owners.id'))
    entries = db.relationship('ConceptQueueEntry', backref='concept_queues', lazy=True)

    def __repr__(self):
        return '<ConceptQueue id:{}, name:{}, capacity:{}, latitude:{}, longitude:{}>'.\
            format(self.id, self.name, self.capacity, self.latitude, self.longitude)

    def serialize(self):
        return {
            'id': self._id,
            'name': self._name,
            'capacity': self._capacity,
            # 'queue': list(map(lambda c: c.serialize(), self._queue))
            'actualClientId':  self.actualClient.id,
            'latitude': self._latitude,
            'longitude': self._longitude
        }
#
# class ConceptQueue:
#     class_counter = 0
#
#     def __init__(self, name, capacity):
#         self._id = ConceptQueue.class_counter + 1
#         self._name = name
#         self._capacity = capacity
#         self._queue = []
#         self._actualClientId = 0
#         self._latitude = 0
#         self._longitude = 0
#         ConceptQueue.class_counter += 1
#
#     # GETTERS
#
#     def id(self):
#         return self._id
#
#     def name(self):
#         return self._name
#
#     def capacity(self):
#         return self._capacity
#
#     def queue(self):
#         return self._queue
#
#     def latiude(self):
#         return self._latitude
#
#     def longitude(self):
#         return self._longitude
#
#     def actualClientId(self):
#         return self._actualClientId
#     # OTHER
#
#     def next(self):
#         return self._queue[0]  #Chequear si existe
#
#     def enqueue(self, client):
#         self._queue.append(client)  #Chequear si existe la cola
#
#     def dequeue(self, database):
#         if len(self._queue) < 1:
#             self._actualClientId = 0
#             return 0
#         else:
#             if self._actualClientId != 0:
#                 old_client = database.getClient(self._actualClientId)
#                 old_client.removeFromShopQueue(self._actualClientId)
#             self._actualClientId = self._queue.pop(0).id()
#             searched_client = database.getClient(self._actualClientId)
#             return searched_client
#
#     def position(self, client_id):
#         if self._actualClientId == client_id:
#             return 0
#         else:
#             return list(map(lambda c: c.id(), self._queue)).index(client_id) + 1
#
#     def serialize(self):
#         return {
#             'id': self._id,
#             'name': self._name,
#             'capacity': self._capacity,
#             'queue': list(map(lambda c: c.serialize(), self._queue)),
#             'actualClient':  self._actualClientId,
#             'latitude': self._latitude,
#             'longitude': self._longitude
#         }
