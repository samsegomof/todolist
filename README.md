# Дипломная работа курса Skypro по специальности Python разработчик.

### Описание проекта:
 - Todolist - планировщик задач по работе с целями и возможностью отслеживания прогресса по ним.
### Технологии:
![version](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![version](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![version](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
---
## Запуск проекта:
 - установить зависимости `pip install -r requirements.txt`
 - поднять контейнер: `docker-compose up -d`

### Переменные окружения:
 - в корневой директории проекта нужно создать файл `.env` и объявить в нем следующие переменные:
 - `DEBUG=True/False` - в зависимости от потребности дебагера Django.
 - `SECRET_KEY='<Секретный ключ Django проекта>'`
 - `DATABASE_URL=psql://<имя пользователя>:<пароль пользователя>@<ip адрес>:<порт>/<имя базы>`

### Запуск сервера:
 - Инициализировать миграции `./manage.py makemigrations`
 - Применить их `./manage.py migrate`
 - Запустить сервер `./manage.py runserver`
---
## Для проверки создать суперпользователя:
 - `./manage.py createsuperuser`

 - Перейти по `http://127.0.0.1:8000/admin` - логин и пароль который указан при создании суперпользователя.
---
 - Январь 2023
 - Семён Шемагонов
---

