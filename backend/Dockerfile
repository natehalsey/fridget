FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./fridget /code/fridget
CMD ["uvicorn", "fridget.base.fridget:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "81"]
