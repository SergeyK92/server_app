# server Django API

API для управления пользователями и заказами

API Endpoints
GET api/users/ - список всех пользователей

POST api/users/ - создать нового пользователя

GET api/users/{id}/ - получить пользователя по ID

PUT api/users/{id}/ - обновить пользователя

GET api/orders/ - список всех заказов

POST api/orders/ - создать новый заказ

GET api/orders/{id}/ - получить заказ по ID

PUT api/orders/{id}/ - обновить заказ



## Запуск проекта

1. Клонируйте репозиторий проекта https://github.com/SergeyK92/server_app.git

2. ВНИМАНИЕ!!!
2.1. Убедитесь, что Docker установлен и запущен на вашей системе
2.2. Миграции в БД выполнятся автоматически.
2.2 После запуска контейнеров приложение будет доступно по адресу:
    http://localhost:8000/api/users/ - список всех пользователей
    http://localhost:8000/api/orders/ - список всех заказов и т.д.


3. Запустите контейнеры:
```bash
docker-compose up --build
