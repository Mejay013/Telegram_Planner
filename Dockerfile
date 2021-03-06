 # set base image (host OS)
FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install -r requirements.txt

CMD [ "python3","main.py" ]

