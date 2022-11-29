# Starting the dev environment
## Frontend Development Only
Use ```REACT_APP_API_URL="http://fridget.co:81" yarn start``` to run local frontend and use server backend

## Frontend and Backend

Follow the instructions in `Running the Backend`, then  follow the instructions in `running the frontend`.

# Deployment

ssh into the deployment server and cd in the fridget directory, pull the latest from main.

run `docker compose build && docker compose up -d`

# Running the Backend

Go to backend dir ```cd backend```

## Starting the virtual environment

```. script/bootstrap```, creates the virtual environment and installs the necessary dependancies.

## Starting the backend

Run the script ```. script/run``` to start the app.

Server address: http://localhost:8000 in your web browser.
Go to http://localhost:8000/docs for Swagger docs.

# Running the Frontend

Go to frontend dir ```cd frontend```

## Starting the UI

Run ```yarn install```
Run ```yarn start``` 

Go to http://localhost:3000 in your web browser.


# Database
cd into the `backend` folder.

## Migrations 

### WARNING WE ARE EDITING OUR LIVE DATABASE DURING LOCAL ONLY RUN AFTER SCHEMA CHANGES ###
Run: ```. script/dbupgrade "upgrade message"``` to autogenerate a revision file. Afterward run the migrations with ```alembic upgrade head```.

## Viewing database tables

Download DBeaver, contact for database access. 
