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
            self.actualClientId = old_entry.clientId # El delete de arriba elimina el primero de arriba haciendo que el atendido sea el nuevo en la pos 0
            old_entry.delete()
            db.session.commit()
            return self.actualClientId

    def remove_client(self, client_id):
        entry_to_delete = self.__entry_for(client_id)
        if entry_to_delete is not None:
            clientId_in_queue = entry_to_delete.clientId
            entry_to_delete.delete()
            return clientId_in_queue
        else:
            return None

    def is_empty(self):
        return len(self.entries) == 0

    def are_clients_behind(self, client_id):
        searched_entry = self.__entry_for(client_id)
        return self.entries.index(searched_entry) + 1 != len(self.entries)

    def swap_client(self, client_id):
        searched_entry = self.__entry_for(client_id)
        index_of_client = self.entries.index(searched_entry)
        client_to_push_back = self.entries[index_of_client]
        client_to_push_up = self.entries[index_of_client + 1]
        client_backup_id = client_to_push_up.clientId
        client_to_push_up.clientId = client_to_push_back.clientId
        client_to_push_back.clientId = client_backup_id
        db.session.commit()

    # private methods

    def __entry_for(self, client_id):
        return next((entry for entry in self.entries if entry.clientId == client_id), None)