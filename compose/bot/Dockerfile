FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/base.txt base.txt
COPY requirements/production.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir -p $HOME
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY . .

ENTRYPOINT ["python", "main.py"]

RUN rm -rf /var/cache/apt/*
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm -rf /etc/apk/cache