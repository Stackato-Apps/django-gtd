python manage.py syncdb --noinput
python manage.py migrate --noinput
# Create the admin user
python manage.py createsuperuser --username=admin --email=admin@mydomain.com --noinput
python manage.py changepassword2 admin secret123
