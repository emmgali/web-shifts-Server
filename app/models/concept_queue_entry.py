from wsgi import db


class ConceptQueueEntry(db.Model):
    __tablename__ = 'concept_queues_entries'
    id = db.Column(db.Integer, primary_key=True)
    clientId = db.Column(db.Integer, db.ForeignKey('clients.id'))
    conceptQueueId = db.Column(db.Integer, db.ForeignKey('concept_queues.id'))
    state = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<ConceptQueueEntry id:{}, clientId:{}, conceptQueueId:{}, state:{}>'.\
            format(self.id, self.clientId, self.conceptQueueId, self.state)

    def serialize(self):
        return {
            'id': self.id,
            'clientId': self.clientId,
            'conceptQueueId': self.conceptQueueId,
            'state': self.state
        }

    def get_client_id(self):
        return self.clientId

    def get_queue_id(self):
        return self.conceptQueueId

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
