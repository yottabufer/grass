from fastapi import APIRouter, Depends, status
from tasks.storage import Storage
from tasks.depends import get_storage
from tasks.service import TaskManager

router = APIRouter(prefix='/tasks')


@router.get('/', status_code=status.HTTP_200_OK)
async def tasks(storage: Storage = Depends(get_storage)):
    """
    Эндпоинт для получения списка задач
    :param storage: Актуальный storage
    """
    task_manager = TaskManager(storage)
    return await task_manager.get_tasks()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_task(task: dict, storage: Storage = Depends(get_storage)):
    """
    Эндпоинт для создания новой задачи
    :param task: Данные задачи
    :param storage: Актуальный storage
    """
    task_manager = TaskManager(storage)
    await task_manager.create_task(task)
    return task


@router.get("/docs")
async def get_swagger_ui_html():
    """
    Эндпоинт для отображения документации swagger
    """
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Docs",
    )

