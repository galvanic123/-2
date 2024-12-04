import json

import requests
from abc import ABC, abstractmethod


class AbstractJobService(ABC):
    @abstractmethod
    def get_jobs(self, search_query):
        pass

class HhJobService(AbstractJobService):
    """Класс реализует подключение к сервисам поиска вакансий"""
    def __init__(self, url: str) -> None:
        self.url = url

    def connect_to_api(self):
        """Функция реализует подключение к сервису ХХ,
        возвращает статус подключения к сервису"""
        response = requests.get(self.url)
        return response.status_code

    def get_jobs(self, params=None) -> str:
        """Функция возвращает вакансии сервиса ХХ если параметр
        не передан, по умолчанию будет None"""
        response = requests.get(self.url)
        return json.dumps(response.json(), ensure_ascii=False, indent=4)
