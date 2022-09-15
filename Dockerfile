FROM python:3.10

WORKDIR /app


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install pipenv
RUN pipenv install typing-extensions

COPY Pipfile.lock Pipfile.lock

RUN pipenv sync

EXPOSE 8000

CMD pipenv run uvicorn web:app --reload --host 0.0.0.0

COPY web /app