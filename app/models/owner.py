from app.models.user import *


class Owner(User):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    ownedQueues = db.relationship('ConceptQueue', backref='owners', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'owner',
    }

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'owned_queues': list(map(lambda q: q.id, self.ownedQueues))
        }