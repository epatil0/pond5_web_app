FROM ubuntu:latest
MAINTAINER Ekta Patil
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN mkdir web_app
COPY .  web_app/
WORKDIR web_app/pond_web_service
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
