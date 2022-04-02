FROM python:3.8-alpine

LABEL author=brrruski
LABEL email=sizhe4real@gmail.com

RUN pip install pipenv

WORKDIR /app

COPY ./ ./

RUN pipenv install

ENTRYPOINT ["python", "./app.py"]