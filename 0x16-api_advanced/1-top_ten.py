#!/usr/bin/python3
"""function that returns the top 10 topics for a given subreddit"""
import requests


def top_ten(subreddit):
    """Gets top 10 subreddit topics
       Args:
           subreddit (str): name of subreddit
       Returns:
           Top 10 topics
    """
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get('{}{}/hot?limit=10'
                            .format(base_url, subreddit), headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        print('None')
        return

    else:
        for data in response.json().get('data').get('children'):
            print(data.get('data').get('title'))
