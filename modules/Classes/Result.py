# -*- coding: utf-8 -*-
import simplejson
class Result:
	def __init__(self, messages, domains):
		self.messages = messages
		self.domains = domains

	def _asdict(self):
		return self.__dict__

	def toJSON(self):
		return simplejson.dumps(self.__dict__, ensure_ascii=False)