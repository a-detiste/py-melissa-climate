#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Magnus Knutas'


class ApiException(Exception):

    def __init__(self, *args):
        self._message = args[0]
        self._status_code = args[1]

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code
