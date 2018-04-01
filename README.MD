# Number Factorizer

Client-server application for decomposing numbers into prime factors

## Установка

Запуск приложения на Windows 10. Крайне желательно установить приложение в корень диска, например, путь может быть: "C:\number_factorizer\" во избежание ошибок.

### Python

Установка Python https://www.python.org/downloads/ или https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64.exe (исполняемый файл для Windows x86 и x64). Скачать и установить Python 3.6.2 для своей версии Windows, добавив Python к системной переменной PATH.

### Django

Установка Django версии 2.0.2 через pip. Ввести команду в cmd:
```
python -m pip install django~=2.0.2
```

### Запуск сервера

Запустить файл run_server.bat. Если не заработало, или появилась ошибка, то открыть командную строку и написать:
```
cd %директория_с_файлом_manage.py%
```
```
python manage.py runserver
```

### Открытие браузера

Открыть браузер по адресу: http://127.0.0.1:8000/

### Остановка сервера

Для того, чтобы остановить сервер, нужно использовать сочетание клавиш CTRL-BREAK, развернув командную строку