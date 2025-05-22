mkdir company
cd company
python3 -m venv .venv
source .venv/bin/activate  //for ubuntu

(.venv) $ python -m pip install django~=5.0.0 
(.venv) $ python -m pip install black
(.venv) $ django-admin startproject django_project .
(.venv) $ python manage.py startapp pages

- add "pages" in the installed app in the settings.py
- add a template folder in the upper directory
- add "DIRS": [BASE_DIR / "templates"],  # new in the settings templates
- add .html file in the templates
- create views.py in the pages, and add the .html file in the templates
- add the url in the urls.py

