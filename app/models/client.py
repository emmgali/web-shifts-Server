from app.models.user import *


class Client(User):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    queuesBeingAttended = db.relationship('ConceptQueue', backref='clients', lazy=True)
    shopQueuesEntries = db.relationship('ConceptQueueEntry', backref='clients', lazy=True)
    shopQueues = db.relationship('ConceptQueue', secondary='concept_queues_entries')
    externalId = db.Column(db.Integer)
    sourceId = db.Column(db.Integer)


    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'shopQueues': list(map(lambda q: q.id, self.shopQueues)),
            'externalId': self.externalId,
            'sourceId': self.sourceId
        }

    def setExternalParameters(self, external_id, source_id):
        self.externalId = external_id
        self.sourceId = source_id
        db.session.commit()

    def all_queues(self):
        return self.shopQueues + self.queuesBeingAttended

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return
