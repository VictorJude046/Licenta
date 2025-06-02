
FROM python:3.13-slim AS production




ENV PYTHONUNBUFFERED=1

WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY DjangoProject2 ./DjangoProject2

EXPOSE 8000

FROM production AS development


COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install --no-cache-dir -r ./requirements/dev.txt


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]