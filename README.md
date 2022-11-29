# Starting the dev environment
## Frontend only
Use ```REACT_APP_API_URL="http://fridget.co:81" npm start``` to run local frontend and use server backend


## Deploying to the server environment

ssh into the ubuntu server and cd in the fridget directory, pull the latest from main.

run `docker compose build && docker compose down && docker compose up -d`

# Running the Backend

Go to backend dir ```cd backend```

## Starting the virtual environment

```. script/bootstrap```, creates the virtual environment and installs the necessary dependancies.

## Database
### WARNING WE ARE EDITING OUR LIVE DATABASE DURING LOCAL ONLY RUN AFTER SCHEMA CHANGES ###
Run: ```. script/dbupgrade "upgrade message"``` to autogenerate a revision file. Afterward run the migrations with ```alembic upgrade head```.

## Viewing database tables

Download DBeaver, contact for database access. 

click finish.

## Starting the app

Run the script ```. script/run``` to start the app.

Server address: http://localhost:8000 in your web browser.
Go to http://localhost:8000/docs for Sawgger docs.

# Running the Frontend

Go to frontend dir ```cd frontend```

## Starting the UI

Run ```npm install```
Run ```npm start``` 

Go to http://localhost:3000 in your web browser.
