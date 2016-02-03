# coding=utf-8

from tvdb import authentication
from tvdb.session import TVDB

with TVDB() as tvdb:
    resp = tvdb.login(apikey='frog')
    print(resp.json().get('Error'))
    print(resp.request.body)
