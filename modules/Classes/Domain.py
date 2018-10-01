import json
class Domain:
	def __init__(self):
		self.fqdn = ""
		self.purchasable = ""
		self.price = ""
		self.no_info = False

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)