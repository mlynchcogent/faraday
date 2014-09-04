#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Faraday Penetration Test IDE - Community Version
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information

'''
import uuid

class CommandRunInformation(object):
    """Command Run information object containing:
        command, parameters, time, workspace, etc."""
    class_signature = "CommandRunInformation"

    def __init__(self, **kwargs):
        self._id = uuid.uuid4().hex
        self.type = self.__class__.__name__
        for k, v in kwargs.items():
            setattr(self, k, v)

    def getID(self):
        return self._id

    def setID(self, id):
        return self._id

    def toDict(self):
        return self.__dict__

    def fromDict(self, dictt):
        for k, v in dictt.items():
            setattr(self, k, v)
        return self
