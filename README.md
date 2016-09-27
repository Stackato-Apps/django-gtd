# Django GTD

A sample *Getting Things Done* (GTD) app using MySQL and the Django admin
interface. To create projects, actions, context or make any modifications, use
the Django admin URL at ``http://<app-url>/admin/``.

## Local development

    pypm install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manager.py runserver

## Deploying to HPE Helion Stackato

Push to the cloud, and then initialize the database:

    cf push

After deploying run the following to create an admin user [cf ssh](http://docs.cloudfoundry.org/devguide/deploy-apps/ssh-apps.html) into the application instance and run:

    python manage.py createsuperuser

Visit <your-app-url> to see the list of tasks. Visit <your-app-url>/admin/ to modify tasks, projects and contexts.
 
## Want to use PostgreSQL?

To use mysql instead of postgresql on production, you need to make only a few
changes before pushing (or updating) your app:

  * In manifest.yml, replace `mysql` with `postgresql` under *services*.
  * In manifest.yml, replace `mysql-python` with `psycopg2` under *requirements*.
