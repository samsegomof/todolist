# Дипломная работа курса Skypro по специальности Python разработчик.

### Описание проекта:
 - Todolist - планировщик задач по работе с целями и возможностью отслеживания прогресса по ним.
 - В приложении реализованы следующие функции:
 - регистрация,
 - вход/выход,
 - получение и обновление профиля,
 - смена пароля,
 - вход через социальную сеть VK.
 - для быстрого просмотра и создания целей доступен бот по ссылке: https://t.me/tdlst_bot

### Технологии:
![version](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![version](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![version](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
---
## Запуск проекта:
 - установить зависимости `pip install -r requirements.txt`
 - поднять контейнер: `docker-compose up -d`

### Переменные окружения:
 - в корневой директории проекта нужно создать файл `.env` и заполнить его на примере файла `.env.example`
 

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

