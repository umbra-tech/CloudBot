FROM python:3.12

RUN mkdir /opt/cloudbot
COPY . /opt/cloudbot
WORKDIR /opt/cloudbot

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "cloudbot" ]