## Instructions
- install virtual environment 
    - `pip install virtualenv`
- make virtualenv
    - `python -m venv env`
- activate the virtualenv
    - `venv\Scripts\activate`
- install the requirements
    - `pip install -r requirements.txt`
- make the migrations and migrate
    - `python manage.py makemigrations`
    - `python manage.py migrate`



## This repo has two branches

> main branch 
    
In this branch provided json data has been fetched from a local json file with pagination to prevent the memory load.


> sqlModel branch 

In this branch sql server implementation added through model called Trade. I have used sqlLite for the better portability and it's compatible with any other sql server. For the testing purpose I have also added a command called seed_data.

- Seed the data
- `python manage.py seed_data`


## Run the server `python manage.py runserver`

### API endpoints
> GET
- `http://127.0.0.1:8000/api/trades?page=1&limit=10`


This API endpoint is available for both (json and sql) versions

