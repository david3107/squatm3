import json
import urllib.parse
from modules.Classes import Domain

def print_text_to_console(msg):
	print(msg)

def print_json_to_console(messages, domains):
	data = {}
	data['messages'] = messages
	data['domains'] = []
	for d in domains:
		data['domains'].append(d.toJSON())
	print(json.dumps(data)) 