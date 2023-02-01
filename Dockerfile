FROM ubuntu:22.04


RUN apt-get update 
RUN apt-get install -y python3 python3-pip

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install -y python3-tk

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

RUN apt -y install ffmpeg

EXPOSE 5000

CMD ["python3", "main.py"]