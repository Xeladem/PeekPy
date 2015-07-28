# -*- coding: utf-8 -*-
from .exception import RedisServiceException


class RedisService(object):

    REDIS_MAP = {"folder": "folder:{folder_id}",
                 "links": "links:{folder_id}",
                 "link": "link:{link_id}",
                 "tags": "tags:{folder_id}",
                 "tag": "tag:{tag_id}"}

    def __init__(self, redis_server):
        """
            Init the redis service with an
            existing redis connection
        """
        if redis_server is None:
            raise RedisServiceException("Redis Service -- connection not set")
        else:
            self.rs = redis_server
