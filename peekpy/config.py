# -*- coding: utf-8 -*-

from path import path

from .utils import INSTANCE_FOLDER_PATH


class BaseConfig(object):

    PROJECT = "PeekPy"
    PROJECT_ROOT = path(__file__).parent.parent.abspath()

    DEBUG = False
    TESTING = False

    ADMINS = ['youremail@yourdomain.com']

    SECRET_KEY = 'secret key'

    LOG_FOLDER = path(INSTANCE_FOLDER_PATH) / 'logs'
    LOG_FOLDER.makedirs_p()


class DefaultConfig(BaseConfig):
    DEBUG = True

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379


class TestingConfig(BaseConfig):
    TESTING = True