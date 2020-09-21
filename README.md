# ZIP Airlines API

Browsable API using Django Rest Framework

### Get Started

_**Note:** To install the dependencies of the project make sure Python 3 is installed._

### Installation
Setup project environment using virtualenv.

```
python3 -m venv env
```

Install project dependencies using pip. 

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Migrate the models and run the development server.
```
python manage.py migrate
python manage.py runserver
```

Access the API via Postman by entering `localhost:8000/api`

### Technologies
* Django 3.1.1
* Python 3
* SQLite3 Database

### JSON Format
```
[
    {
        "airplane_id": 1,
        "passenger_count: 5
    }
]
```