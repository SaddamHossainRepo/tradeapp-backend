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
    -`python manage.py makemigrations`
    -`python manage.py migrate`



## This repo has two branches

### main branch has used the json file to load data



### the sqlModel has use the sqlLite3 database
- Seed the data
- `python manage.py seed_data`


## Run the server `python manage.py runserver`

### API endpoints
GET
- `http://127.0.0.1:8000/api/trades?page=1&limit=10`

- 


