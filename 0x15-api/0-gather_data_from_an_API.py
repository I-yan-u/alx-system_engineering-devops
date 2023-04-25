#!/usr/bin/python3
""" Script to assess API data from select url"""
import requests
import sys

if __name__ == "__main__":
	url = 'https://jsonplaceholder.typicode.com/'
	user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
	tasks = requests.get(url + "todos", params={'userId': sys.argv[1]}).json()

	completed = [t.get("title") for t in tasks if t.get("completed") is True]

	print("Employee {} is done with tasks({}/{})".format(user.get("name"),
							     len(completed), len(tasks)))
	for task in completed:
		print("\t {}".format(task))
