# Questionnaire

Сервис по работе с опросами

### Требования


[Python](https://www.python.org/downloads/) v3.7 +  для запуска.
Установите зависимости и виртуальное окружение и запустите сервер.

```sh
$ pip install virtualenv
$ virtualenv 'название виртуального окружения'
$ venv 'название виртуального окружения'/Scripts(или bin для linux)/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

Запуск через докер, если установлен

1. В корневой директории проекта создайте образ командой docker build -t <тут введите имя образа> .
2. Запустите контейнер командой docker run -it -p 8000:8000 <имя образа>
3. Приложение будет доступно в браузере по адресу http://localhost:8000/.


Так же для удобной работы лучше всего использовать [Postman](https://www.postman.com/downloads/)

## Доступные методы
| endpoint | Тип запроса | Описание |
| :--- | :--- | :--- | 
| api-auth/login/| GET | Авторизация|
| api-auth/logout/| GET | Выход|
| api/v1/poll/create/ | GET | Создание опроса|
| api/v1/update/{poll_id}/ | PATCH, DELETE  | Удаление, частичное/пoлное редактирование опроса по id|
| api/v1/poll/view/ | GET | Получение списка опросов|
| api/v1/poll/view/active/ | GET | Получение списка опросов активных опросов|
| api/v1/question/create/ | POST | Создание вопроса
| api/v1/q/posts/ | POST | Создание вопроса через viewset
| api/v1/question/update/{question_id}/ | PATCH, DELETE | Изменение вопроса|
| api/v1/choice/create/ | POST | Создание выбора ответа |
| api/v1/choice/update/{choice_id}/ | PATCH, DELETE  | Изменение выбора ответа
| api/v1/answer/create/ | POST | Добавление ответа|
| api/v1/answer/view/{user_id}/ | GET | Получение ответов пользователя|
| api/v1/answer/update/{answer_id}/ | PATCH, DELETE  | Редактирование ответа по id

## Примеры
Все API ендпоинты возвращают JSON представление получаемых, созданных или отредактированных объектов.

Пример запроса POST на api-auth/login/

    {
        "username": "user"
        "password": "password",
    }

Пример ответа: 

    Status: 200 OK

Пример GET ответа на api/v1/poll/view/active/

    [
    {
        "id": 1,
        "name": "name",
        "pub_date": "2020-11-11T07:44:39.336161Z",
        "end_date": "2020-11-29T12:12:12Z",
        "description": "description",
        "questions": [
            {
                "id": 1,
                "poll": 1,
                "q_text": "q_text",
                "q_type": "q_type",
                "choices": []
            },
        ]
    }
    ]



## Авторы

* **Vladimir Svetlakov** - [svvladimir-ru](https://github.com/svvladimir-ru)
