# Django GTD

A sample *Getting Things Done* (GTD) app using PostgreSQL and the Django admin
interface. To create projects, actions, context or make any modifications, use
the Django admin URL at ``http://gtd.stackato.local/admin/``.

## Local development

    pypm install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manager.py runserver

## Deploying to Stackato

Push to the cloud, and then initialize the database:

    stackato push -n
    stackato run python manage.py syncdb  # prompts for admin password
    stackato run python manage.py migrate

NOTE: if you get a postgres DatabaseError ``terminating connection due
to administrator command``, simply re-run the previous command.
    
Visit http://gtd.stackato.local/ to see the list of tasks. Visit http://gtd.stackato.local/admin/ to modify tasks, projects and contexts.
 
## Want to use MySQL?

To use mysql instead of postgresql on production, you need to make only a few
changes before pushing (or updating) your app:

  * In requirements.txt, replace `psycopg2` with `mysql-python`
  * In settings.py, replace `django.db.backends.postgresql_psycopg2` with
    `django.db.backends.mysql`
  * In settings.py, replace `vcap_services['postgresql-8.4'][0]` with
    `vcap_services['mysql-5.1'][0]`
  * In stackato.yml, replace `postgresql` with `mysql.
