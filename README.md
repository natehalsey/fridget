# Running the Backend

## Starting the virtual environment

```. script/bootstrap```, creates the virtual environment and installs the necessary dependancies.

## Database

 Run: ```alembic revision --autogenerate -m "update message goes here"``` to autogenerate a revision file. Afterward run the migrations with ```alembic upgrade head```.

## Viewing database tables

Install sqlite3, and run it with ```sqlite3```. Type: ```.open db.sqlite``` to open the database, and to view tables: ```.tables```.

## Starting the app

Run the script ```. script/run``` to start the app. Go to localhost:8000 in your web browser.