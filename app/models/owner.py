from wsgi import db
from . import association_tables


class Owner(db.User):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    ownedQueues = db.relationship(
        "ConceptQueue",
        secondary=association_tables.owners_conceptqueues_table,
        back_populates="owners")

    __mapper_args__ = {
        'polymorphic_identity': 'owners',
    }

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'owned_queues': list(map(lambda q: q.id, self._ownedQueues))
        }

# from . import user as u
#
#
# class Owner(u.User):
#     def __init__(self, name):
#         super().__init__(name, "Owner"),
#         self._ownedQueues = []
#
#     def ownedQueues(self):
#         return self._ownedQueues
#
#     def serialize(self):
#         return {
#             'id': self._id,
#             'name': self._name,
#             'type': self._type,
#             'owned_queues': list(map(lambda q: q.id(), self._ownedQueues))
#         }