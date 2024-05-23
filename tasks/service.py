from datetime import datetime
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from tasks.storage import Storage
from tasks.models import Task


class TaskManager:
    """Менеджер для управления список задач"""

    def __init__(self, storage: Storage):
        self.storage = storage

    async def get_tasks(self) -> dict:
        """
        Метод для получения списка задач
        :return: Список задач в виде словаря
        Тут возвращался return await self.storage.read(), а не список задач
        Так же в типизации стояло, что должен возвращаться список, но в тестах должен быть словарь,
        да и FastAPI работает со словарями
        """
        tasks = await self.storage.read()
        return {"tasks": tasks.get('tasks', [])}

    async def create_task(self, task_data: dict):
        """
        Метод для созадния задачи
        :param task_data: Данные задачи для создания
        Тут вообще было пусто, написал всё сам
        """

        task_data = dict(task_data)
        tasks = await self.storage.read()

        if not task_data.get('title'):
            # Я долго разбирался почему строчка снизу не работает((
            # return JSONResponse(status_code=400, content={"detail": "The title cannot be empty"})
            raise HTTPException(status_code=400, detail='The title cannot be empty')

        if task_data.get('completed') not in (True, False):
            raise HTTPException(status_code=400, detail='Completed type error')

        if tasks['tasks']:
            max_id = max(task['id'] for task in tasks['tasks'])
            new_id = max_id + 1
        else:
            new_id = 1

        now = datetime.now()
        task_data['created_at'] = now.strftime("%Y-%m-%dT%H:%M:%S")
        task_data['updated_at'] = now.strftime("%Y-%m-%dT%H:%M:%S")
        task_data['id'] = new_id
        tasks['tasks'].append(task_data)
        # Простенькая валидация, что словарь task_data подходит под модель Task
        try:
            task = Task(**task_data)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())
        await self.storage.save(tasks=tasks['tasks'])
        return JSONResponse(status_code=201, content=task_data)
