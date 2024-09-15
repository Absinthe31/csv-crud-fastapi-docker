FROM python:3.12.5-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y patch

RUN pip3 install -r requirements.txt

RUN pip3 install fastapi[standard]

COPY . .

CMD fastapi run csv_crud.py