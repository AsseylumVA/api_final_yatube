##API для соц. сети [Yatube](https://github.com/AsseylumVA/hw05_final "Yatube")


### Функционал:
Данный проект является CRUD-приложением и реализует работу с публикациями, комментариями, собществами, подписками и авторизацией.

После запуска проекта, документация доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AsseylumVA/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
