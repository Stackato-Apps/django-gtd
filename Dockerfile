FROM ubuntu:12.04

COPY . /src

RUN cd /src && apt-get update && apt-get install -y python-dev && apt-get install -y libmysqlclient-dev && apt-get install -y python-pip && pip install -r requirements.txt

CMD cd /src && python manage.py syncdb --noinput && python manage.py migrate --noinput && python manage.py collectstatic --noinput && echo "from django.contrib.auth.models import User; import os; User.objects.create_superuser(os.environ['USERNAME'], os.environ['EMAIL'], os.environ['PASS'])" | ./manage.py shell && gunicorn wsgi:application
