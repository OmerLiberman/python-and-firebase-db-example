import requests
import json

ROUTE_USERS = "???"
ROUTE_TASKS = "???"
ROUTE_TASKS_BY_USER = "???"


# Users
def create_user(name, username, password):
	data = json.dumps({
		'name': name,
		'username': username,
		'password': password
	})
	res = requests.post(ROUTE_USERS.format(username=username), data)
	if res.status_code == 200:
		print("User has been created.")
	else:
		print("Error has been occurred.")


def delete_user(username):
	res = requests.delete(ROUTE_USERS.format(username=username))
	if res.status_code == 200:
		print("User has been deleted.")
	else:
		print("Error has been occurred.")


# Tasks
def create_task(username, task_name, task_content):
	data = json.dumps({
		'task_name': task_name,
		'task_content': task_content
	})
	res = requests.post(ROUTE_TASKS.format(username=username, task_name=task_name), data)
	if res.status_code == 200:
		print("Task has been created.")
	else:
		print("Error has been occurred.")


def delete_task(username, task_name):
	res = requests.delete(ROUTE_TASKS.format(username=username, task_name=task_name))
	if res.status_code == 200:
		print("Task has been deleted.")
	else:
		print("Error has been occurred.")


def get_all_tasks_by_username(username):
	res = requests.get(ROUTE_TASKS_BY_USER.format(username=username))
	data = json.loads(res.content)
	tasks = []
	for e in data:
		if type(e) == dict:
			for k, v in e.items():
				tasks.append(v)
	return tasks
