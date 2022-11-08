FROM python:3.10.8-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

ADD ./requeriments.txt /usr/src/app/
ADD ./desafio_vue_django/ /usr/src/app/
RUN cd /usr/src/app/ && \
    pip install --no-cache-dir -r ./requeriments.txt && \
    rm ./requeriments.txt

WORKDIR /usr/src/app/

EXPOSE 8000

ENTRYPOINT python /usr/src/app/manage.py runserver 0.0.0.0:8000
