from wsgi import db


class ConceptQueue(db.Model):
    __tablename__ = 'concept_queues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    capacity = db.Column(db.Integer)
    latitude = db.Column(db.Numeric(10, 3))
    longitude = db.Column(db.Numeric(10, 3))
    actualClientId = db.Column(db.Integer, db.ForeignKey('clients.id'))
    ownerId = db.Column(db.Integer, db.ForeignKey('owners.id'))
    entries = db.relationship('ConceptQueueEntry', backref='concept_queues', lazy=True)


    def __repr__(self):
        return '<ConceptQueue id:{}, name:{}, capacity:{}, latitude:{}, longitude:{}>'.\
            format(self.id, self.name, self.capacity, self.latitude, self.longitude)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity,
            # 'queue': list(map(lambda c: c.serialize(), self._queue))
            'actualClientId':  self.actualClientId,
            'latitude': float(self.latitude),
            'longitude': float(self.longitude),
            'entriesAmount': len(self.entries)
        }

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return "Queue deleted successfully"

    def position(self, client_id):
        if (self.actualClientId is not None) and (self.actualClientId.id == client_id):
            return 0
        else:
            return list(map(lambda c: c.clientId, self.entries)).index(client_id) + 1

    def has_client(self, client_id):
        return (next((entry for entry in self.entries if entry.clientId == client_id), None)) is not None

    def dequeue_and_attend(self):
        if len(self.entries) == 0:
            if self.actualClientId is not None:
                self.actualClientId = None
                db.session.commit()
                return None
            else:
                return None
        else:
            old_entry = self.entries[0]
            self.actualClientId = old_entry.get_client_id() # El delete de arriba elimina el primero de arriba haciendo que el atendido sea el nuevo en la pos 0
            old_entry.delete()
            db.session.commit()
            return self.actualClientId

    def get_entries(self):
        return self.entries

    def remove_client(self, client_id):
        entry_to_delete = next((entry for entry in self.entries if entry.clientId == client_id), None)
        if entry_to_delete is not None:
            clientId_in_queue = entry_to_delete.clientId
            entry_to_delete.delete()
            return clientId_in_queue
        else:
            return None

    def is_empty(self):
        return len(self.entries) == 0

    def are_clients_behind(self, client_id):
        searched_entry = next((entry for entry in self.entries if entry.clientId == client_id), None)
        return self.entries.index(searched_entry) + 1 != len(self.entries)

    def swap_client(self, client_id):
        searched_entry = next((entry for entry in self.entries if entry.clientId == client_id), None)
        index_of_client = self.entries.index(searched_entry)
        client_to_push_back = self.entries[index_of_client]
        client_to_push_up = self.entries[index_of_client + 1]
        client_backup_id = client_to_push_up.clientId
        client_to_push_up.clientId = client_to_push_back.clientId
        client_to_push_back.clientId = client_backup_id
        db.session.commit()




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
#             'actualClientId':  self._actualClientId,
#             'latitude': self._latitude,
#             'longitude': self._longitude
#         }