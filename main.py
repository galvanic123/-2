from src.hh_api import HeadHunterAPI

if __name__ == '__main__':
    hh_api = HeadHunterAPI()
    hh_api.load_vacancies("электромеханик")
    hh_vacancies = hh_api.get_vacancies()
    print(*hh_vacancies, sep="\n")