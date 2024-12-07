import json
import os
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from config import DATA_DIR


class Employee(ABC):
    """Абстрактный родительский класс для обработки файла"""
    @abstractmethod
    def read_file(self):
        pass


    @abstractmethod
    def write_file(self, ser_vacs):
        pass


    @abstractmethod
    def add_vacancy(self, vacancy):
        pass


    @abstractmethod
    def del_vacancy(self):
        pass


class JSONSaver(Employee):
    """Класс для работы с файлом со списком вакансий"""
    filename_value = "vacancies.json"
    def __init__(self, filename=filename_value):
        self.vacs_list = []
        self.__filename = os.path.join(DATA_DIR, filename)


    @property
    def filename(self):
        return self.__filename


    def read_file(self):
        """Функция чтения файла. Проверяет, есть ли файл и при наличии сохраняет список объектов."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as f:
                vacs = json.load(f)
            self.vacs_list = [Vacancy(i) for i in vacs]
        return self.vacs_list


    def write_file(self, vacs_obj: list):
        """Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy."""
        vacs_list = []
        for i in vacs_obj:
            vacs_list.append(
                {
                    "name": Vacancy(i).name,
                    "alternate_url": Vacancy(i).link,
                    "salary": {"from": Vacancy(i).salary},
                    "snippet": {"responsibility": Vacancy(i).description},
                    "area": {"name": Vacancy(i).area},
                }
            )
        with open(self.filename, 'w', encoding='UTF-8') as f:
            json.dump(vacs_list, f, ensure_ascii=False, indent=4)


    def add_vacancy(self, vacancy):
        pass


    def del_vacancy(self):
        with open(self.filename, 'w') as f:
            pass
