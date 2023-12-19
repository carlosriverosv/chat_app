# About the app

This is a chat API application built using `Python 3.9`, `Django` and `DjangoRestFramework`. The Postman collection for the API is in the `postman_collection.json` file. 
This app contains 3 models: `User`, `Conversation`, and `Message`. All endpoints are open which mean they don't expect a token in the request neither they check for permissions to execute a request.

## Building and running the application

### If it's for the first time

Duplicate the `.env.example` file and change it's name to `.env`.
To build and run the application for the first time, open a terminal located in the root folder and run:

`make setup`

this command will pull a postgres image from Docker Hub if it's not in the system and then will spin up a container for the database called `db` and expose the port `5432`. A database called `wizzer` will also be created. It then will build the `api` image using the `Dockerfile` file and will expose the port `8000`. This app will connect to the postgres database. 
Then the migrations will apply to the database and all the tables will be created.

If you run `docker ps`, you should see both containers (db and api) up and running.

### For other times

If you need to install new requirements go to the explanation `for installing new requirements`

Open a terminal located in the root folder and run:

`make start`

If you run `docker ps`, you should see both containers (db and api) up and running.


### For creating migrations

Open a terminal located in the root folder and run:

`make migrations`

This command should create any new migrations pending to be created and put them inside the `migrations` folder.

### For running migrations

Open a terminal located in the root folder and run:

`make migrate`

This command will apply the migrations to the `db` making changes to it.

### For stopping the containers

Open a terminal located in the root folder and run:

`make stop`

This command will stop both containers (db and api).

### For installing new requirements

Open a terminal located in the root folder and run:

`make update_requirements`

This command will stop the containers, delete the api image and create it again.


### Running tests

Open a terminal located in the root folder and run:

`make tests`

This command will run all the tests located in the `chat/tests` folder.

### Coverage report

Open a terminal located in the root folder and run:

`make coverage`

This command will display the coverage report 
