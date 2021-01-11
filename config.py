import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or  'you-could-never-ever-guess'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'DBMU'
    MYSQL_DATABASE_PASSWORD = 'GameWinner!11'
    MYSQL_DATABASE_DB = 'dndblog'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://DBMU:GameWinner!11@localhost/dndblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
