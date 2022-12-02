# Starting the dev environment


### Running the Backend

Go to backend dir ```cd backend```  .
```. script/bootstrap``` create the virtual environment and installs the necessary dependencies.  
Run the script ```. script/run``` to start the app.  

Server address: http://localhost:8000.   
Go to http://localhost:8000/docs for API docs.  

### Running the Frontend

Go to frontend dir ```cd frontend```.  
Run ```yarn install```.  
Run ```yarn start```.   

Go to http://localhost:3000 in your web browser.  

## Frontend Development Only
Use ```REACT_APP_API_URL="http://fridget.co:81" yarn start``` to run local frontend and use server backend.  
Note Authentication does not work with this setup

# Deployment

ssh into the deployment server and cd in the ```Fridget``` directory, pull the new release branch.

run `docker compose build && docker compose up -d` to redeploy server

# Database

## Migrations 

#### WARNING WE ARE EDITING OUR LIVE DATABASE DURING LOCAL ONLY RUN AFTER SCHEMA CHANGES ####
Run: ```. script/dbupgrade "upgrade message"``` to autogenerate a revision file. Afterward run the migrations with ```alembic upgrade head```.

## Viewing database tables

Download DBeaver, contact for database access. 
