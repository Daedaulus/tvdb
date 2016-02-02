# coding=utf-8

import json
import requests


def get_from_file(filename=None):
    with open(filename) as swag_file:
        swag = json.load(swag_file)
    return swag


def get_from_url(url=None):
    resp = requests.get(url)
    return resp.json() if resp.ok else None
