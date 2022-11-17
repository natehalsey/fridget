FROM python:3.9
 
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./db.sqlite /code/db.sqlite
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations
COPY ./fridget /code/fridget

CMD ["uvicorn", "fridget.fridget:app", "--host", "0.0.0.0", "--port", "80"]