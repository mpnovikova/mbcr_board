# MBTA #
## Prerequisites ##
* [Python 3.7.4](https://www.python.org/downloads/)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [git](https://git-scm.com/downloads)
* [flask](http://flask.pocoo.org/)

## Installation ##
To install requirements in a virtual environment begin by running

    $ virtualenv venv

Followed by installing requirements:

    $ pip install -r requirements.txt

This is a Flask application which comes with some built-in commands. To start this application, run 

    $ python -m flask run
    
## Solution ##
This application is a web application which runs on `localhost:5000` and responds to following requests:

```GET /<stop_id>```

Where `<stop_id>` could only be one of the following values:

    * `place-north` North Station 
    * `place-sstat` South Station
    * `place-bbsta` Back Bay
  
Will list all MBCR trains in the following format:

    Time	Destination	Train#	Track#	Status
