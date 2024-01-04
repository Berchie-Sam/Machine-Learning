FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system 

COPY ["model_C=0.01.bin", "predict.py", "./"]

EXPOSE 9696
