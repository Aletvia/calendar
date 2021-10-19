# Calendar of activities test
API Rest which implements a system of a calendar.

## Instalation
Requeriments:
- Entorno virtual (venv)
- Python 3.7, pip

### Enviroment

This environment let ​make changes in the API. Follow the next steps:

1. Create virtual environment (_venv_)
```shell script
virtualenv venv
```
2. Activate virtual environment
```shell script
source venv/bin/activate
```
3. Packages install
```shell script
(venv) pip install -r PATH/requirements.txt
```

With these steps we generate access to the libraries necessary for the development of the project.

1. It is necessary to carry out the corresponding migrations, execute the following command in the terminal within the same folder:
```shell script
python src/manage.py makemigrations
python src/manage.py migrate
```
2. To run the API tests, run the following command in the terminal within the same folder:
```shell script
src/manage.py test runserver
```
3. If everything is fine, you could access the API.



**Endpoints available:**

- Create a new property
POST: http://127.0.0.1:8000/api/v1/properties/

- List existing products
GET: http://127.0.0.1:8000/api/v1/activities/<start_date>/<end_date>/
GET: http://127.0.0.1:8000/api/v1/activities/<average_date>/
GET: http://127.0.0.1:8000/api/v1/activities/<status>/

- Create a new activity
POST: http://127.0.0.1:8000/api/v1/activities/

- Update an existing activity
PUT: http://127.0.0.1:8000/api/v1/activities/
