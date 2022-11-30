# Starting the dev environment

## Local Frontend Development
Use ```REACT_APP_API_URL="http://fridget.co:81" yarn start``` to run local frontend and use prod server backend

## Local Frontend and Backend Development

```source ./local_dev_env.sh```. Set development environment variables

## Frontend and Backend

Follow the instructions in `Running the Backend`, then  follow the instructions in `running the frontend`.

### Running the Backend

 ```cd backend```. Go to backend dir
```. script/bootstrap```. Creates the virtual environment and installs the necessary dependancies.
```. script/run```. Start the backend.

Server address: http://localhost:8000
Go to http://localhost:8000/docs for Swagger docs.

### Running the Frontend

```cd frontend```. Go to frontend dir 
```yarn install```. Install dependencies
```yarn start```. Start the frontend

Go to http://localhost:3000 in your web browser.

## Using Docker
```docker compose build && docker compose up -d```

# Deployment

ssh into the deployment server and cd in the fridget directory, pull the release branch from main.
```cd Fridget```. Go to Fridget directory
```git pull origin <release-branch>```. Pull release branch from github
```docker compose build && docker compose up -d```. Reload the server

# Database

## Viewing database tables

Download DBeaver, contact for database access. 

## Migrations 

### WARNING WE ARE EDITING OUR LIVE DATABASE DURING LOCAL ONLY RUN AFTER SCHEMA CHANGES ###
Run: ```. script/dbupgrade "upgrade message"``` to autogenerate a revision file. Afterward run the migrations with ```alembic upgrade head```.

## Viewing database tables

Download DBeaver, contact for database access. 
