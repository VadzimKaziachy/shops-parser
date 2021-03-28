# Environment variables

[Русский](../ru/enviroment.md) | **English**

Part of the project settings is taken from environment variables. 
To define them, create a **.env** file next to **docker-compose.yml** and write the data there in this format: **VARIABLE=value**.

The following variables are available:

- **COMPOSE_PROJECT_NAME** - sets the project name. This value is prepended along with the service name to the container on start up. 
For example, if your project name is **myapp** and it includes two services **db** and **web**, 
then Compose starts containers named **myapp_db_1** and **myapp_web_1** respectively;
- **COMPOSE_PROJECT_DIR** - path to the project folder;
- **RABBITMQ_PORT** - the port on which RabbitMQ is running;
- **RABBITMQ_USER** - username;
- **RABBITMQ_HOST** - the host on which RabbitMQ is running;
- **RABBITMQ_QUEUE** - the queue in which the data will sent;
- **RABBITMQ_PASSWORD** - user password;
- **RABBITMQ_VIRTUALHOST** - the virtual host to be used.