# coding=utf-8
"""
TVDB Api v2

Authentication : Obtaining and refreshing your JWT token
Episodes : Information about a specific episode
Languages : Available languages and information
Search : Search for a particular series
Series : Information about a specific series
Updates : Series that have been recently updated
Users : Routes for handling user data
"""

import logging
# from datetime import datetime, timedelta

import requests

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)


class Authentication:
    """
    Obtaining and refreshing your JWT token
    
    post /login
    get /refresh_token
    """
    def __init__(self):
        pass

    @staticmethod
    def login(apikey, username=None, password=None):
        """
        Returns a session token to be included in the rest of the requests.

        Note that API key authentication is required for all subsequent requests
        and user auth is required for routes in the User section

        :param apikey: required for all subsequent requests
        :param username: required for routes in the User section
        :param password: required for routes in the User section
        :returns:
        """
        display_credentials = True
        url = 'https://api-beta.thetvdb.com/login'
        credentials = {
            'apikey': apikey,
            'username': username,
            'userpass': password,
        }
        log.debug('Attempting login: {login_type} {url} {credentials}'.format
                  (login_type='apikey login' if not username and password else 'user login', url=url,
                   credentials=credentials if display_credentials else '<login credentials redacted>',))
        return requests.post(url, json=credentials)

    @staticmethod
    def refresh(token):
        """
        Refreshes your current, valid JWT token and returns a new token.

        Hit this route so that you do not have to post to /login with your API key
        and credentials once you have already been authenticated.

        :param token: to refresh
        :return:
        """
        authorization = {'Authorization': 'Bearer {token}'.format(token=token)}
        return requests.get('https://api-beta.thetvdb.com/refresh_token', headers=authorization)

    @staticmethod
    def authenticate(apikey=None, username=None, password=None, token=None):
        return Authentication.refresh(token) or Authentication.login(apikey, username, password)


class Episodes:
    """
    Information about a specific episode

    get /episodes/{id}
    """


class Languages:
    """
    Available languages and information

    get /languages
    get /languages/{id}
    """


class Search:
    """
    Search for a particular series

    get /search/series
    get /search/series/params
    """


class Series:
    """
    Information about a specific series

    get /series/{id}
    head /series/{id}
    get /series/{id}/actors
    get /series/{id}/episodes
    get /series/{id}/episodes/query
    get /series/{id}/episodes/query/params
    get /series/{id}/episodes/summary
    get /series/{id}/filter
    get /series/{id}/filter/params
    get /series/{id}/images
    get /series/{id}/images/query
    get /series/{id}/images/query/params
    """


class Updates:
    """
    Series that have been recently updated

    get /updated/query
    get /updated/query/params
    """


class Users:
    """
    Routes for handling user data

    get /user
    get /user/favorites
    delete /user/favorites/{id}
    put /user/favorites/{id}
    get /user/ratings
    get /user/ratings/query
    get /user/ratings/query/params
    put /user/ratings/{itemType}/{itemId}/{itemRating}
    delete /user/ratings/{itemType}/{itemId} 
    """

resp = Authentication.authenticate('DE1EAEFAD0F4587D', 'knossos', 'tvdb2147')
