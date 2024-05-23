FROM python:3.11-slim AS builder
RUN pip install poetry
COPY pyproject.toml poetry.lock ./

# Установка зависимостей через Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

FROM python:3.11-slim
COPY --from=builder /usr/local /usr/local
WORKDIR /app
COPY . .
CMD ["uvicorn", "tasks.main:app", "--host", "0.0.0.0", "--port", "9000"]