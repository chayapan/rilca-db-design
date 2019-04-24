 FROM python:2.7-alpine
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
RUN mkdir /app/PADocument
 WORKDIR /app
 ADD requirements.txt /app/
 RUN pip install -r requirements.txt
 ADD . /app/
