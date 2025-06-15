Веб-сервис для управления движением денежных средств (ДДС)


Скопируйте репозиторий https://github.com/matveinovikov1000/cash_flow_management/tree/feature


Для корректного запуска проекта установите зависимости 
(список зависимостей указан в pyproject.toml):

poetry add django
poetry add djangorestframework
poetry add python-dotenv
poetry add psycopg2-binary
poetry add django-filter

При использовании pip install для установки, зависимости необходимо сохранить в файле 
requirements.txt в корне проекта


Для настройки необходимо добавить в корне проекта файл .env, в котором указать
(пример в .env.example)(в проекте используется PostgreSQL):

SECRET_KEY - ключ проекта (генирируется в config/settings)
POSTGRES_DB - имя БД
POSTGRES_USER - имя пользователя БД
POSTGRES_PASSWORD - пароль для БД
POSTGRES_HOST - хост БД
POSTGRES_PORT - порт БД


Для запуска приложения необходимо:
- запустить миграции
    python manage.py makemigrations
    python manage.py migrate
- создать суперюзера для доступа в админку
    python manage.py createsuperuser
- запустить приложение на локальном сервере
    python manage.py runserver

Админка доступна тут http://127.0.0.1:8000/admin/
(для входа необходмо указать username и password суперюзера)
