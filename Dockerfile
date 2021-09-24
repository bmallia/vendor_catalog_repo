FROM python:3.8

##dont generate pyc files
ENV PYTHONDONTWRITEBYTECODE 1
##message log dont stand in buffer
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

