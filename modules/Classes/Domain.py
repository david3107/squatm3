# -*- coding: utf-8 -*-
import simplejson
class Domain:
	def __init__(self):
		self.fqdn = ""
		self.purchasable = ""
		self.price = ""
		self.no_info = False

	def _asdict(self):
		return self.__dict__

	def toJSON(self):
		return simplejson.dumps(self.__dict__, ensure_ascii=False)