FROM alang/django:2.0-python3

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get -y install python-mysqldb

ENV DJANGO_MIGRATE=true
RUN mkdir /tmp/requirements
COPY ./requirements /tmp/requirements

RUN pip install -r /tmp/requirements/local.txt

WORKDIR /usr/django/app
ENTRYPOINT ["/bin/bash", "-c"]
