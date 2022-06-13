class Config(object):
    SECRET_KEY ='#'
    DEBUG = True
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = '#'
    MAIL_PASSWORD = '#'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = '#'
    FLASK_ENV = 'development'
    TESTING = False
    MAIL_SUPPRESS_SEND = False

class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG= False
    SESSION_COOKIE_SECURE = True    
    FLASK_ENV = 'production'
