A simple donut shop website with an SQLite database, made with Python (Django framework). Functional, but also in the process of being improved.

To make the website work:
1. Ensure that you have Python (version 3.10+) and PIP installed.
2. Activate the virtual environment: Open the terminal, navigate to the parent folder containing 'fn_donutshop' (i.e. if saved in "./Desktop/myproject/", type in the command ```cd './myproject'```), and...
    - MAC OS: ```source donutshop/bin/activate```
    - Windows: ```python3 -m venv env```
    ```env/Scripts/Activate.ps1```
    This creates a virtual environment named "env".
3. Install required modules: 
```python3 -m pip install -r requirements.txt```
4. Navigate to the folder "./fn_donutshop/donut_shop_website".
5. Make migrations to the database:
```python3 manage.py makemigrations donuts```
```python3 manage.py migrate```
6. Run the server: ```python3 manage.py runserver```. Visit http://127.0.0.1:8000/ on your browser.
