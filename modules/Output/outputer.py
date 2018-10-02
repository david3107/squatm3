import simplejson
import urllib.parse
from modules.Classes import Domain, Result


def print_text_to_console(msg):
	print(msg)

def print_json_to_console(messages, domains):
	res = Result.Result(messages, domains)
	print(simplejson.dumps(res, ensure_ascii=False))
	
