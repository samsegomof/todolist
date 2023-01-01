# Diploma of the Skypro course in the specialty Python developer.

### Project description:
- Todolist is a task planner for working with goals and the ability to track progress on them.
### Technologies:
 - Django==4.0.1
 - djangorestframework
 - Postgresql
---
## Start project:
 - install dependensies `pip install -r requirements.txt`
 - start database from directory /postgresql: `docker-compose up -d`

### Environment variables:
 In the root directory of the project, you need to create a .env file and declare the following variables in it:
  - `DEBUG=True/False` - depending on the need of the Django debugger.
  - `SECRET_KEY='<Secret key by Django project>'`
  - `DATABASE_URL=psql://<username>:<password>@<host>:<prot>/<name_of_database>`

### Start server:
 - Initialize migrations `./manage.py makemigrations`
 - Apply them `./manage.py migrate`
 - Run server `./manage.py runserver`

### To test, create a superuser:
 - `./manage.py createsuperuser`
 - Go to `http://127.0.0.1:8000/admin` - the login and password that was specified when creating the superuser.

---
### Simon Shemagonov
### November 2022
### telegram: @sssimooon
### +79173454545
### simon1239@yandex.ru
---