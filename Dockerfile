FROM python:2.7-alpine
ENV PYTHONUNBUFFERED 1

# add gcc
RUN apk add --no-cache gcc musl-dev

# set timezone
RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Bangkok /etc/localtime
RUN date

# prepare python requirements
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# install app
RUN mkdir /app
ADD rilca-web /app/

EXPOSE 8000
WORKDIR /app

# Add any custom, static environment variables needed by Django or your settings file here:
# ENV DJANGO_SETTINGS_MODULE=my_project.settings.deploy

# uWSGI configuration (customize as needed):
# ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=my_project/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
# RUN DATABASE_URL=none /venv/bin/python manage.py collectstatic --noinput

# Start uWSGI
# CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]

CMD python manage.py runserver 0.0.0.0:8000
