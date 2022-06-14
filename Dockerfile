FROM python:3.8

RUN ls

RUN mkdir server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./src/server /usr/src/server

COPY ./requirements.txt /usr/src/server

WORKDIR /usr/src/server

RUN pip install -U pip

RUN pip install -r requirements.txt

EXPOSE 50051

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/server"

CMD ["python", "main.py"]