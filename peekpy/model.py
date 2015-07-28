# -*- coding: utf-8 -*-
import datetime


class Folder(object):

    def __init__(self, **kwargs):
        """ """
        self.id = kwargs['id']
        self.title = kwargs['title']

        #Set the status of the folder
        if 'is_read_only' not in kwargs:
            self.is_read_only = False
        else:
            self.is_read_only = kwargs['is_read_only']

        self.password = kwargs['password']

        if 'add_date' not in kwargs:
            #Init the date for the new folder
            self.add_date = str(datetime.datetime.now())
        else:
            self.add_date = kwargs['add_date']

        if 'last_edit' not in kwargs:
            self.last_edit = self.add_date
        else:
            self.last_edit = kwargs['add_date']

        #Set the Time to live of the folder
        # 0 is for unlimited
        if 'ttl' not in kwargs:
            self.ttl = 0
        else:
            self.ttl = kwargs['ttl']


class Link(object):

    def __init__(self, **kwargs):
        """ """
        self.id = kwargs['id']
        self.owner = kwargs['owner']
        self.type = kwargs['type']
        self.url = kwargs['url']
        self.title = kwargs['title']
        self.author = kwargs['author']
        self.raw_content = kwargs['raw_content']
        self.formatted_content = kwargs['formatted_content']

        if 'add_date' not in kwargs:
            #Init the date for the new link
            self.add_date = str(datetime.datetime.now())
        else:
            self.add_date = kwargs['add_date']

        if 'last_edit' not in kwargs:
            self.last_edit = self.add_date
        else:
            self.last_edit = kwargs['add_date']

        #Set the Time to live of the link
        # 0 is for unlimited
        if 'ttl' not in kwargs:
            self.ttl = 0
        else:
            self.ttl = kwargs['ttl']

