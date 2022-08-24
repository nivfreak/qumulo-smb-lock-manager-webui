# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

ADD "https://github.com/nivfreak/qumulo-smb-lock-manager/archive/master.tar.gz" master.tar.gz
RUN tar -xzf master.tar.gz

WORKDIR /qumulo-smb-lock-manager-master
COPY . /qumulo-smb-lock-manager-master

RUN pip3 install -r web-requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "gunicorn.sh"]
