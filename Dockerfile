FROM python:3.8.5-alpine
ENV PYTHONUNBUFFERED 1

ADD config/requirements.txt /home/config/requirements.txt
RUN pip install -r /home/config/requirements.txt

RUN mkdir home/knu_notice
RUN mkdir /static
ADD config/requirements.txt /home/config/requirements.txt
RUN pip install -r /home/config/requirements.txt
WORKDIR /home/knu_notice
ADD . /home/knu_notice