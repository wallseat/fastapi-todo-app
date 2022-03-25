FROM python:3.10-alpine

ENV POSTGRES_DSN ''
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    gcc \
    g++ \
    libffi-dev \
    musl-dev

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /code/app
COPY ./migrations /code/migrations
COPY alembic.ini /code
