## Документация по проекту

Тестовый суперпользователь с именем admin и паролем 123admin (т.к. пароль должен быть 8 или более символов)

Для запуска проекта необходимо:

* Установить зависимости:

```bash
pip install -r requirements.txt
```

* Провести миграцию:

```bash
python manage.py migrate
```

* Загрузить тестовые данные:

```bash
python manage.py loaddata fixtures.json
```

* Выполнить следующие команды:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
