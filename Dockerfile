FROM python:3.8-slim

LABEL author=brrruski
LABEL email=sizhe4real@gmail.com

RUN pip install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple/

WORKDIR /app

COPY Pipfile* ./

RUN pipenv install

COPY ./ ./

ENTRYPOINT ["pipenv", "run", " python", "./app.py"]