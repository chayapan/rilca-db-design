# rilca-db-design
RILCA database design prototype application.

# Development:

Python/Django

### Install Python libraries:

pip install -r requirements.txt

### Start Django development server:

python manage.py runserver

Go to port 8000, for example http://127.0.0.1:8000/items


### MariaDB

See this repo for Docker and SQL

https://github.com/sylviachadha/rilca/blob/master/Tables.sql


# Staging/Preview

## Docker / Docker Compose

The app is serve at HTTP port 4023.

http://DOCKER_MACHINE:4023

### Build:

docker-compose build

### Run the app:

docker-compose up -d

### Stop the app:

docker-compose down

### Remove:

docker-compose rm

### Get into Container shell

docker exec -it rilcadbdesign_web_1 sh
