# Notes API

Проект "Notes API" — REST API для работы с заметками, реализован на FastAPI с использованием PostgreSQL и SQLAlchemy.

## Описание
API позволяет создавать, получать, обновлять и удалять заметки. Каждая заметка содержит заголовок, текст, статус выполнения и временные метки.

## Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone <URL_репозитория>
cd <папка_проекта>
```

### 2. Настройка переменных окружения
Создайте файл `.env` по примеру `.env.example` и укажите данные для подключения к базе данных.

### 3. Запуск с Docker
```bash
docker-compose up --build
```
Проект будет доступен по адресу `http://localhost:8000`.

### 4. Запуск без Docker
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Эндпоинты

### Получение всех заметок
```
GET /notes
```
Возвращает список всех заметок.

### Получение заметки по ID
```
GET /notes/{note_id}
```
Возвращает заметку по её ID. Если заметка не найдена, возвращает 404.

### Создание новой заметки
```
POST /notes
```
Тело запроса:
```json
{
  "title": "Заголовок",
  "content": "Текст заметки"
}
```
Создаёт новую заметку с `done=false` по умолчанию.

### Обновление заметки
```
PUT /notes/{note_id}
```
Тело запроса может содержать любое сочетание полей:
```json
{
  "title": "Новый заголовок",
  "content": "Новый текст",
  "done": true
}
```

### Удаление заметки
```
DELETE /notes/{note_id}
```
Удаляет заметку по ID. Возвращает 204 No Content.

## Документация API
FastAPI автоматически генерирует документацию по адресу:
```
http://localhost:8000/docs  # Swagger UI
http://localhost:8000/redoc # Redoc
```

## Структура проекта
```
app/
  main.py        # Точка входа
  models.py      # SQLAlchemy модели
  schemas.py     # Pydantic схемы
  crud.py        # Логика CRUD
  database.py    # Подключение к БД
  routers.py     # Маршруты для заметок
requirements.txt
Dockerfile
docker-compose.yml
.env.example
README.md
```

## Примечания
- Фильтрация по полю `done` пока не реализована.
- Тесты с pytest пока не написаны.

## Контакты
Если возникнут вопросы, пишите на email: <ваш_email>

