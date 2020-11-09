# ucs_satellite_data
Get UCS Satellite Data: Python, Flask, with open(), next(), for, render_template()

![screen capture](/screen_capture.png)

## Virtual Environment

Below, Python's `venv` module was used to create the virtual environment which was used to create this application. So, the contents of this repo can be dropped into such a virtual env. To create a virtual environment, enter the following in a Unix-like terminal emulator:

```sh
$ python -m venv your_new_venv
$ cd your_new_venv/
$ source bin/activate
```

`cd`
: used to navigate to `your_new_venv/` project root directory

`source`
: reads and executes the `activate` command located in the `bin/` directory which activates the newly created virtual environment.

After the virtual env is created, and the repo is then added to it, the local directory structure should look something like the following:

```sh
bin/
data/
include/
lib/
lib64 -> lib/
templates/
ucs_satellite.py
```

`data/`
: directory where the satellite TSV data file is stored

`templates/`
: directory where Jinja template is stored

`ucs_satellite.py`
: the Flask application

## Flask Application

```python
#! /bin/python3
'''Get satellite data, then render template to browser.'''
import csv
from flask import Flask
from flask import render_template

APP = Flask(__name__)  # Flask instance
SAT_DATA = []  # satellite data

@APP.route('/')  # route to root
def get_sat_data():
    '''Get satellite data, then render template to browser.'''
    with open('data/ucs_satellite_data.tsv', 'r') as tsv_read:
        csv_read = csv.reader(tsv_read, delimiter='\t')  # init CSV reader obj
        next(csv_read)  # skip column header row
        for row in csv_read:
            SAT_DATA.append(row)  # append CSV record to SAT_DATA
    return render_template('template.htm', sat_data=SAT_DATA)  # render template

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=3000)  # if standalone
```

## Unix Shebang

The Unix shebang consists of a number sign followed by an exclamation mark (`#!`). In a Unix-like operating system, the shebang allows an executable text file to run in a terminal emulator. In this case, the shebang line reads `#! /bin/python3`. And since the following lines of text are Python instructions, they will be parsed and executed as such.

Also, the Python script could be executed in a Unix-like terminal emulator by entering `$ ./ucs_satellite.py`.

## Documentation

```python
'''Get satellite data, then render template to browser.'''
```

Since there is only one method in the module, the documentation for module and method are identical. As can be seen in the Python interactive shell:

```python
>>> __doc__
'Get satellite data, then render template to browser.'
>>> get_sat_data.__doc__
'Get satellite data, then render template to browser.'
```

## Imports

```python
from csv import reader
from flask import Flask
from flask import render_template
```

`from csv import reader`
: `csv.reader` returns a CSV reader object that iterates over CSV records in CSV database file

`from flask import Flask`
: `Flask()` is used to initialize a Flask instance

`render_template`
: `render_template()` renders a Jinja2 template, including variables passed to the template engine

## Flask Instance, Data Variable

```python
APP = Flask(__name__)
SAT_DATA = []
```

`APP = Flask(__name__)`
: initializes the Flask instance of the app

`SAT_DATA = []`
: `SAT_DATA` contains lines of data from the CSV record which will be passed to the Jinja2 template

## Route Decorator

```python
@APP.route('/')
```

`@APP.route('/')`
: decorator which registers view function&mdash;which shows entries in CSV database; `'/'` indicates root path

## View Function

```python
def get_sat_data():
    '''Get satellite data, then render template to browser.'''
    with open('data/ucs_satellite_data.tsv', 'r') as tsv_read:
        csv_read = reader(tsv_read, delimiter='\t')
        next(csv_read)
        for row in csv_read:
            SAT_DATA.append(row)
```

`def get_sat_data():`
: defines view function

`with open('data/ucs_satellite_data.tsv', 'r') as tsv_read:`
: defines `with open()` block where the TSV database file is opened in read mode

`csv_read = csv.reader(tsv_read, delimiter='\t')`
: reader object which iterates over lines of the given TSV reader object while converting tabs to commas

`next(csv_read)`
: advances the CSV reader object to its second record in order to skip the column header titles

`for row in csv_read:`
: defines `for` loop which iterates through each line of CSV reader object

`SAT_DATA.append(row)`
: appends each line of the CSV reader object to the `SAT_DATA` variable

`return render_template('template.htm', sat_data=SAT_DATA)`
: `render_template()` receives a Jinja2 template and the satellite data and then renders the template

## Run App

```python
if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=3000)  # if standalone
```

The block above runs the app if `__name__` equals `__main__`, which would be the case if the app was executed as a standalone application.
