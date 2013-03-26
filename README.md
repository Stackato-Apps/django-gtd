# Django GTD

A sample *Getting Things Done* (GTD) app using PostgreSQL, Memcached and the Django admin
interface. To create projects, actions, context or make any modifications, use
the Django admin URL at ``http://<app-url>/admin/``.

## Local development

    pypm install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manager.py runserver

## Deploying to Stackato

Push to the cloud, and then initialize the database:

    stackato push -n

Visit http://gtd.stackato.local/ to see the list of tasks. Visit http://gtd.stackato.local/admin/ to modify tasks, projects and contexts.
 
## Want to use PostgreSQL?

To use mysql instead of postgresql on production, you need to make only a few
changes before pushing (or updating) your app:

  * In stackato.yml, replace `mysql` with `postgresql` under *services*.
  * In stackato.yml, replace `mysql-python` with `psycopg2` under *requirements*.
