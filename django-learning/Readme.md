# Windows
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $ python -m pip install django~=5.0.0
(.venv) $ python -m pip install black

# macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 -m pip install django~=5.0.0
(.venv) $ python3 -m pip install black

# Ubuntu
$ python3 -m venv .venv
$ source venv/bin/activate
deactivate
pip install django
django-admin --version
django-admin startproject django_project .
pip install django==3.2  # Replace 3.2 with your desired version
python manage.py migrate
python manage.py runserver


python manage.py startapp pages