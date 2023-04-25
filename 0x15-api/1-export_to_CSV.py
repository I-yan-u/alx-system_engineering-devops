#!/usr/bin/python3
""" Script to assess API data from select url"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    tasks = requests.get(url + "todos", params={'userId': user_id}).json()
    username = user.get("username")

    completed = [t.get("title") for t in tasks if t.get("completed") is True]

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in tasks]
