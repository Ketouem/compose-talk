FROM python:3-alpine

ENV APP_DIR /app

EXPOSE 5000

COPY . ${APP_DIR}
WORKDIR ${APP_DIR}

RUN pip install --upgrade pip && pip install -r requirements.txt
