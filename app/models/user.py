from wsgi import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)

    __mapper_args__ = {
        'polymorphic_identity': 'users',
        'polymorphic_on': type
    }

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
        }

    def __repr__(self):
        return '<User id:{}, name:{}, type:{}>'.format(self.id, self.name, self.type)


# class User:
#     class_counter = 0
#
#     def __init__(self, name, type):
#         self._id = User.class_counter + 1
#         self._name = name
#         self._type = type
#         User.class_counter += 1
#
#     def id(self):
#         return self._id
#
#     def name(self):
#         return self._name
#
#     def type(self):
#         return self._type
#
#     def serialize(self):
#         return {
#             'id': self._id,
#             'name': self._name,
#             'type': self._type,
#         }
