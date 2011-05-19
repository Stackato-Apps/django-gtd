Deploying to Stackato
=====================

1. ``vmc push djangogtd`` (add a mysql service)

2. Initialize the db::

    vmc run djangogtd "python manage.py syncdb --noinput"
    vmc run djangogtd "python manage.py migrate --noinput"

3. # XXX: can't run `manage.py createsuperuser --noinput` as it
   doesn't set a password

4. Open the djangogtd URL, you should see the app albeit with empty data.
