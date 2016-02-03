# coding=utf-8

"""
TVDB  APIv2
"""

from requests import Session
from tvdb import authentication


class TVDB(Session):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._login = authentication.LoginRequest()

    def login(self, apikey=None, username=None, password=None):
        self._login.apikey = apikey or self._login.apikey
        self._login.username = username or self._login.username
        self._login.password = password or self._login.password
        login = self.prepare_request(self._login)
        return self.send(login)
