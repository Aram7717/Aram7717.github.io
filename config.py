class Config(object):
    SECRET_KEY ='jigsaw11235'
    DEBUG = True
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'mraram77@gmail.com'
    MAIL_PASSWORD = 'zljjraljbnlwsjzl'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'mraram77@gmail.com'
    FLASK_ENV = 'development'
    TESTING = False
    MAIL_SUPPRESS_SEND = False

class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG= False
    SESSION_COOKIE_SECURE = True    
    FLASK_ENV = 'production'