FROM python:3.13-slim as production

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirments/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY DjangoProject2 ./DjangoProject2

EXPOSE 8000