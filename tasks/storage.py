import json
import os
from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Абстрактный класс хранилища данных в файловой системе пользователя. Содержит методы для чтения и записи данных.
    """
    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def save(self, **kwargs):
        raise NotImplementedError


class JSONStorage(Storage):
    """
    По заданию в Readme.md описываю минусы JSONStorage:
    1. В Storage методы read и save объявлены как сихрнонные, а в JSONStorage асинхронные
    2. Достаточно сильно "захардкоден" путь к файлу data.json
    3. Не было никакой обработки ошибок
    4. И как я говорил на собеседовании - нет потокобезопасности в при записи/чтении, если начать читать и записывать,
       то может привести к ошибке или потере данных
    5. Возвращаясь к асинхронности изначально указан open, а не aiofiles
    6. Ну и в конце концов - это простой json файл, а не специализированная база данных
    """
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    _path = os.path.join(curr_dir, 'data.json')

    async def read(self) -> dict:
        """
        Метод назывался read_data, не и добавил обработку ошибок
        """
        try:
            with open(self._path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    async def save(self, **kwargs):
        """
        Не был совсем написан метод save
        """
        with open(self._path, 'w') as file:
            json.dump(kwargs, file)
        return None
