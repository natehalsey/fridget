# Running the Backend

## Starting the virtual environment

Run the bootstrap script by running: ```. script/bootstrap```, this will install the required dependancies and put you in a python virtual environment. 

## Database

If making changes to the base.schema (will update tables in our database) run: ```alembic revision --autogenerate -m "update message goes here"```. Afterward run the migrations with ```alembic upgrade head```. If you're getting weird errors, you may need to run migrations.

## Viewing database tables

We can use the command line. Install sqlite3, and run it with ```sqlite3``` in your terminal. While in the ```fridget-app``` directory type: ```.open db.sqlite``` and to view tables: ```.tables```.

## Starting the app

Run the script ```. script/run``` to start the app.
 