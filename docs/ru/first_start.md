# Первый старт

**Русский** | [English](../en/first_start.md)

Вы можете запустить проект **shops-parser** локально использовую **Pipenv**.

### Зависимости

* [pip3](https://github.com/pypa/pip)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Python 3.9](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

### Установка

Прежде всего, установите [Pipenv](https://pypi.org/project/pipenv/), выполните команды:

    pip install pipenv

Перейдите в папку [parser](../../docker/parser) и активируйте среду:

    pipenv shell

Убедитесь, что окружение было создано и активировано.

Далее необходимо установить все необходимые пакеты для приложения.

    pipenv install
    
Следующим шагом является настройка переменных среды.
Вы можете прочитать, как настроить файл переменных среды, в разделе [Переменные среды](enviroment.md)

Далее добавьте переменные в виртуальное окружение:

    export $(cat .env)

После того, как все было настроено, вы можете запустить проект. Перейдите в папку [src](../../src) и выполните комманду:

    scrapyd 
   
Приложение будет работать на порту [6800](http://localhost:6800).