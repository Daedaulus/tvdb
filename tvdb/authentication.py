# coding=utf-8

"""
Authentication : Obtaining and refreshing your JWT token
"""

from requests import Request


class LoginRequest(Request):
    """
    Returns a session token to be included in the rest of the requests.

    Note that API key authentication is required for all subsequent requests
    and user auth is required for routes in the User section
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.method = 'POST'
        self.url = 'https://api-beta.thetvdb.com/login'
        self.status_codes = {
            200: 'Returns a JWT token for use with the rest of the API routes',
            401: 'Invalid credentials and/or API token',
        }

    def json_set(self, key, value):
        if not self.json:
            self.json = {}
        self.json[key] = value

    @property
    def apikey(self):
        return self.json.get('apikey')

    @apikey.setter
    def apikey(self, value):
        self.json_set('apikey', value)

    @property
    def username(self):
        return self.json.get('username')

    @username.setter
    def username(self, value):
        self.json_set('username', value)

    @property
    def password(self):
        return self.json.get('userpass')

    @password.setter
    def password(self, value):
        self.json_set('userpass', value)


def refresh():
    # get /refresh_token
    pass
