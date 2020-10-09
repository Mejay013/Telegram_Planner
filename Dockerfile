 # set base image (host OS)
FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python3","main.py" ]

