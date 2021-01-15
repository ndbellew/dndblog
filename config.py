import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or  'you-could-never-ever-guess'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'DBMU'
    MYSQL_DATABASE_PASSWORD = 'GameWinner!11'
    MYSQL_DATABASE_DB = 'dndblog'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://DBMU:GameWinner!11@localhost/dndblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['superdaggler@gmail.com']
    POSTS_PER_PAGE = 25
