# Starting the dev environment
## Frontend only
Use ```REACT_APP_API_URL="http://fridget.co:81" npm start``` to run local frontend and use server backend


## Deploying to the server environment
# Running the Backend

Go to backend dir ```cd backend```

## Starting the virtual environment

```. script/bootstrap```, creates the virtual environment and installs the necessary dependancies.

## Database

Run: ```. script/dbupgrade "upgrade message"``` to autogenerate a revision file. Afterward run the migrations with ```alembic upgrade head```.

## Viewing database tables

Download DBeaver and select "create new database", select postgres, it will download the drivers.

for host put in 74.119.150.172 for database change to fridget, username: postgres, password: SRql605syVtnpUtP

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
