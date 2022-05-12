FROM python:3.9

WORKDIR /app

# Installing native dependencies
RUN apt-get update && apt-get install -y \
  gdal-bin \
  && rm -rf /var/lib/apt/lists/*

# Installing python libraries
COPY requirements.txt ./
RUN pip install -r requirements.txt && rm requirements.txt

COPY ./src /app/

CMD python manage.py collectstatic --noinput; \
    python manage.py migrate; \
    gunicorn --bind=0.0.0.0 --workers=4 --log-file=- --access-logfile=- cognition.wsgi

