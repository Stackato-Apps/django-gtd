# Django GTD application

## Local development

    pypm install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manager.py runserver

## Deploying to Stackato

    stackato push django-gtd
    stackato run "python manage.py syncdb --noinput"
    stackato run "python manage.py migrate --noinput"

### Limitations

Django admin's superuser creation cannot be automated (note:
``--noinput``), so /admin/ is unusable for this app.
