import os
basedir = os.path.abspath(os.path.dirname(__file__))


# access config with app.config['key']
class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#class TestingConfig(Config):
#    DB_SERVER = 'localhost'
#    DEBUG = True
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

