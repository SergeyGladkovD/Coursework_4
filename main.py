from src.api import HeadHunterAPI
from src.JSONSaver import JSONSaver


def user_interaction():
	while True:
		user_input = input(f'Хотите посмотреть отложенные вакансии нажмите 1\n'
		f'Хотите удалить отложенные вакансии нажмите 2\n'
		f'Хотите начать новый поиск вакансий нажмите 3\n'
		f'Остальные команды прекратят работу программы.\n')
		if user_input == '1':
			print(JSONSaver.read_vacancy())
		elif user_input == '2':
			JSONSaver.delete_vacancy()
			print('Вакансии удалены.')
		elif user_input == '3':
			user_input = input('Какую вакансию вы ищете?')
			hh_api = HeadHunterAPI()
			hh_vacancies = hh_api.get_vacancies(user_input)
			# user_city = input('В каком городе?')

			for i in hh_vacancies:
				print(i)
		else:
			print('Программа завершена.')
			break


if __name__ == "__main__":
	user_interaction()
