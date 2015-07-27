# -*- coding: utf-8 -*-


class BaseConfig(object):
    PROJECT = "PeekPy"
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True