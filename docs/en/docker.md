# Setup with Docker

[Русский](../ru/docker.md) | **English**

### Dependencies

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

The first thing you need to do is set up your environment variables.
You can read how to configure the environment variable file in the section [Environment Variables](enviroment.md)

Next, run the project using Docker:

    cd docker
    docker-compose up --build -d
    
The application will run on port [6800](http://localhost:6800).