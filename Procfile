web: gunicorn A2SL.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn A2SL.wsgi
