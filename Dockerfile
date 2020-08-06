FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir home/crawling
ADD config/requirements.txt /home/config/requirements.txt
RUN pip install -r /home/config/requirements.txt
EXPOSE 50051 50052
WORKDIR /home/crawling