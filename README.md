# Bike Rental Service

Bike Rental Service - это сервис для аренды велосипедов. Он предоставляет RESTful API для выполнения основных операций.

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone <repository_url>
    cd bike_rental_service
    ```

2. Создайте и активируйте виртуальную среду:

    ```sh
    python -m venv venv
    source venv/bin/activate  # для Linux/macOS
    venv\Scripts\activate  # для Windows
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Выполните миграции:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```sh
    python manage.py createsuperuser
    ```

6. Запустите сервер:

    ```sh
    python manage.py runserver
    ```

## Использование

### Регистрация нового пользователя

```http
POST /api/users/register/
Content-Type: application/json

{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "testpassword"
}
```

### Авторизация пользователя

```http
POST /api/token/
Content-Type: application/json

{
  "email": "testuser@example.com",
  "password": "testpassword"
}
```

### Получение списка доступных велосипедов

```http
GET /api/bikes/
Authorization: Bearer <access_token>
```

### Аренда велосипеда

```http
POST /api/bikes/rent/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "bike": 1
}
```

### Возврат велосипеда

```http
PUT /api/bikes/return/<rental_id>/
Content-Type: application/json
Authorization: Bearer <access_token>

{}
```

### Получение истории аренды пользователя

```http
GET /api/bikes/history/
Authorization: Bearer <access_token>
```

## Swagger документация

Swagger документация доступна по адресу [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## Запуск с Docker

1. Создайте файл `.env` в корне проекта и добавьте в него переменные окружения для базы данных и других сервисов.

2. Запустите Docker Compose:

    ```sh
    docker-compose up --build
    ```

3. Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

## Тестирование

1. Запустите тесты:

    ```sh
    python manage.py test
    ```

## CI/CD

CI/CD настроен с использованием GitLab CI. Конфигурация находится в файле `.gitlab-ci.yml`.

## Лицензия

Этот проект лицензирован под лицензией MIT.
