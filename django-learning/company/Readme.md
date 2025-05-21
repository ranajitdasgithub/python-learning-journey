mkdir company
cd company
python3 -m venv .venv
source .venv/bin/activate  //for ubuntu

(.venv) $ python -m pip install django~=5.0.0 
(.venv) $ python -m pip install black
(.venv) $ django-admin startproject django_project .
(.venv) $ python manage.py startapp pages

- add "pages" in the installed app in the settings.py
