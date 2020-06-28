from wsgi import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    type = db.Column(db.String(64), index=True)

    __mapper_args__ = {
        'polymorphic_on': type
    }

    @classmethod
    def filter_by(cls, name, user_type=None):
        if user_type is None:
            return cls.query.filter_by(name=name).all()
        else:
            return cls.query.filter_by(name=name, type=user_type).all()

    def __repr__(self):
        return '<User id:{}, name:{}, type:{}>'.format(self.id, self.name, self.type)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
        }
