from wsgi import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)

    __mapper_args__ = {
        'polymorphic_on': type
    }

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
