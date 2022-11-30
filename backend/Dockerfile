FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

#ENV DATABASE_URL "postgresql://dev:fridget@172.17.0.2:5432/postgres"
#ENV DATABASE_URL "postgresql://postgres:SRql605syVtnpUtP@74.119.150.172:5432/fridget"

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./fridget /code/fridget
CMD ["uvicorn", "fridget.base.fridget:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "81"]
