from wsgi import db


clients_conceptqueues_table = db.Table('association', db.Base.metadata,
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id')),
    db.Column('concept_queue_id', db.Integer, db.ForeignKey('concept_queues.id'))
)

owners_conceptqueues_table = db.Table('association', db.Base.metadata,
    db.Column('owner_id', db.Integer, db.ForeignKey('owners.id')),
    db.Column('concept_queue_id', db.Integer, db.ForeignKey('concept_queues.id'))
)