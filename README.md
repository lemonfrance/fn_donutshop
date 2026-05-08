A simple donut shop website with an SQLite database, made with Python (Django framework). Functional, but also in the process of being improved.

To make the website work:
1. Ensure that you have Python and PIP installed.
2. Activate the virtual environment: Open the terminal, navigate to the folder where the folder 'donutshop' is saved (i.e. if saved in "./Desktop/myproject/", type in the command "cd './myproject'"), and...
    - MAC OS: ... type in "source donutshop/bin/activate".
    - Windows: ... type in "python3 -m venv donutshop_env" then "donutshop_env/Scripts/Activate.ps1".
3. Ensure these modules are installed (python3 -m pip show insertmodulename): django, django-phonenumber-field, django-phonenumbers, Pillow, whitenoise. If not, install them with: python3 -m pip install insertmodulename.
3. Run server: Navigate to "./donutshop/donut_shop_website" and type in "python3 manage.py runserver".
4. Visit http://127.0.0.1:8000/ on your browser.