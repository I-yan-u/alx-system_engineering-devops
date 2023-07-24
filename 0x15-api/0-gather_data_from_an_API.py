#!/usr/bin/python3
""" Accessing API data"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    userId = sys.argv[1]
    user = {"userId": userId}

    req = requests.get(url + 'users/{}'.format(userId)).json()
    req2 = requests.get(url + 'todos/', params=user).json()

    completed = [t.get('title') for t in req2 if t.get('completed') is True]
    user_name = req.get('name')

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, len(completed), len(req2)))
    [print('\t {}'.format(c)) for c in completed]
