#!/usr/bin/python3
"""
Gets amount of subscribers on subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Gets amount of subscribers on subreddit. """
    url = 'https://api.reddit.com/r/'
    header = {'User-Agent': 'Yandev.tech'}
    req = requests.get('{}{}/about'.format(url, subreddit),
                       headers=header, allow_redirects=False)

    if req.status_code != 200:
        return 0
    else:
        response = req.json()
        return response.get('data').get('subscribers')
