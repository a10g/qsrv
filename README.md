# qsrv
A simple quote server



This is a simple Flask application that reads a directory of fortune files and serves a random quote. It provides a simple HTTP REST interface, defaults to ASCII text output for use in shell scripts, supports JSON or HTML output for integration with external applications.


# API Usage:

Send an HTTP GET to the desired URI.

```
/api
Returns API information and usage.
```

```
/api/quote
Returns a random quote from all available fortune databases.
```

```
/api/quote/{database}
Returns a quote from the selected database.
```


To Do:
- Add JSON and HTML outputs
