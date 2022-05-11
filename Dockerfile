FROM python:3.9

WORKDIR /app

# Installing python libraries
COPY requirements.txt ./
RUN pip install -r requirements.txt && rm requirements.txt

COPY ./src /app/

CMD python manage.py collectstatic --noinput; \
    python manage.py migrate; \
    gunicorn --bind=0.0.0.0 --workers=4 --log-file=- --access-logfile=- one_model.wsgi

