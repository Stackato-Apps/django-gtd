# Django GTD application

This is a sample Getting Things Done (GTD) app demonstrating a
databased-backed application making use of the Django admin. To create
projects, actions, context or to make any modifications use the Django
admin located at ``http://<yourapp>.domain.com/admin/``.

Technologies used: Django, MySQL

## Local development

    pypm install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manager.py runserver

## Deploying to Stackato

    stackato push djangogtd
    # Answer "yes" when asked to bind any services and select "mysql"

    stackato run djangogtd "python manage.py syncdb --noinput"
    stackato run djangogtd "python manage.py migrate --noinput"

    # Create the admin user
    stackato run djangogtd "python manage.py createsuperuser --username=admin --email=admin@mydomain.com --noinput"
    stackato run djangogtd "python manage.py changepassword2 admin secret123"

    # Visit the app; go to /admin/ to add tasks, projects and contexts.
 
