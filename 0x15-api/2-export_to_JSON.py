#!/usr/bin/python3
""" Script to assess API data from select url"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    tasks = requests.get(url + "todos", params={'userId': user_id}).json()
    username = user.get("username")

    completed = [t.get("title") for t in tasks if t.get("completed") is True]

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": t.get("title"),
                            "completed": t.get("completed"), "username": username}
                   for t in tasks]}, jsonfile)
