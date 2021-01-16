# simple_api
A Minimal Read-Only REST API auto-generated from SQL SERVER

Includes a root page to navigate the links to each table's endpoint. 

***This is a proof-of-concept and not recommended for any kind of production implementation.***

### Implemented in less than 20 lines of code

| Language                     | files          | blank        | comment           | code |
| ---------------------------- | -------------- | ------------ | ----------------- | ---- |
| Python                       |   1            | 5            | 0                 | 14   |
| HTML                         |   1            | 0            | 0                 | 5    |
| **SUM**:                     |   2            | 5            | 0                 | 19   |


## Getting Started

1. Create a `.env` file and add your database connections parameters as values for the following keys:

```
DB_SERVER=
DB=
DB_SCHEMA=
DB_USER=
DB_PWD=

FLASK_APP=app.py
```

2. Install dependencies

```
$ pipenv install
```

3. Run the server

```
$ pipenv run flask run
```

4. Navigate to the api on localhost: 
- [http://localhost:5000/api](http://localhost:5000/api)