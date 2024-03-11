from abc import ABC
import requests


class AbsHeadHunterAPI(ABC):

	def hh_api(self):
		pass


class HeadHunterAPI(AbsHeadHunterAPI):

	def get_vacancies(self, user_input):
		url = 'https://api.hh.ru/vacancies'
		params = {'text': user_input, 'search_field': 'name', 'per_page': 100}
		response = requests.get(url, params=params)
		return response.json()['items']