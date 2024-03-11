from abc import ABC
import json


class AbsVacancy(ABC):

	def __init__(self):
		pass

	def to_json(self):
		pass

	def compare_vacancy(self):
		pass


class Vacancy(AbsVacancy):

	def __init__(self, name, url, salary, snippet):
		self.name = name
		self.url = url
		self.salary = salary
		self.snippet = snippet

	def to_json(self):
		return json.dumps(vars(self))

	def compare_vacancy(self):
		pass
