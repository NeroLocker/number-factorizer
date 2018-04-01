Number factorizer

Webmath application

Запуск приложения на Windows 10. Крайне желательно распаковать приложение в корень диска, например, путь может быть: "C:\number_factorizer\"

1. Установка Python https://www.python.org/downloads/ или https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64.exe (исполняемый файл для Windows x86 и x64)
	-Скачать и установить Python 3.6.2 для своей версии Windows, добавив Python к системной переменной PATH

2. Установка Django версии 2.0.2 через pip:
	-Ввести команду в cmd: python -m pip install django~=2.0.2

3. Запустить файл run_server.bat
	-Если не заработало, или появилась ошибка, то открыть командную строку и написать:
		1) cd %директория_с_файлом_manage.py%
		2) python manage.py runserver

4. Открыть браузер по адресу: http://127.0.0.1:8000/

5. Для того, чтобы остановить сервер, нужно использовать сочетание клавиш CTRL-BREAK, развернув командную строку