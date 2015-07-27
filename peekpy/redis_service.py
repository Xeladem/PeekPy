# -*- coding: utf-8 -*-
from .exception import RedisServiceException


class RedisService(object):

    def __init__(self, redis_server):
        """
            Init the redis service with an
            existing redis connection
        """
        if redis_server is None:
            raise RedisServiceException("Redis Service -- connection not set")
        else:
            self.rs = redis_server
