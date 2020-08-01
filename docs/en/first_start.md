# Local development

[Русский](../ru/first_start.md) | **English**

You can run the **shops-parser-backend** project locally using **Pipenv**.

### Dependencies

* [pip3](https://github.com/pypa/pip)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Python 3.8](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

### Installation

First of all, installed [Pipenv](https://pypi.org/project/pipenv/),then run the commands:

     pip install pipenv
     
Go in the [parser](../../docker/parser) folder and activate the environment:

    pipenv shell

Make sure that the environment has been created and activated.

Next, you need to install all the necessary packages for the application.

    pipenv install
    
The next step is to configure our local environment variables. 
You can read how to configure the environment variable file in the section [Environment variables](enviroment.md)

After everything has been configured, you can start the project. The first thing you need to do is perform migrations
to set up a database:

Next, add the variables to the virtual environment:

    export $(cat .env)

After everything has been configured, you can start the project. Go to the folder [src](../../src) and run the command:

    scrapyd

The application will run on port [6800](http://localhost:6800).