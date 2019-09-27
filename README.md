# qsrv
A simple quote server



This is a simple Flask application that reads a directory of fortune files and serves a random quote. It provides a simple HTTP REST interface, defaults to ASCII text output for use in shell scripts, supports JSON or HTML output for integration with external applications.

# Requirements:
[Python 3](https://www.python.org).
[Flask](https://palletsprojects.com/p/flask/).
[Virtualenv](https://docs.python-guide.org/dev/virtualenvs/) recommended.


# Local Operation - Development/Testing
```
$ git clone [url]
$ cd qsrv_func
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```
Point your browser at http://localhost:5000/ for the home page, or append one of the routes below for a fortune.

*To Do: include some deployment instructions*


# API Usage:

Send an HTTP GET to the desired URI.

```
/api
Returns API information and usage.
(not yet implemented)
```

```
/api/fortune/random
Returns a random fortune from all available fortune databases.
```

```
/api/fortune/{database}
Returns a fortune from the selected database.
```

```
/api/fortune/list
List all fortunes in database
```

## Examples
```
Get random fortune from terminal:
curl http://localhost:5000/api/fortune/random
```

```
Select fortune from THE MIGHTY MONARCH! fortune file:
curl http://localhost:5000/api/fortune/the-mighty-monarch
```


To Do:
- Add JSON and HTML outputs
