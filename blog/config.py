import os


class BaseConfig(object):
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "v0w_hu@=c65diol%(kp%h6ii&d4(3-vp38f8)2^6jd&qm&@%*+"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    Debug = True


class TestingConfig(BaseConfig):
    TESTING = True