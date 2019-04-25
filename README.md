# Bestpitch_App
Flask app (back end and front end) with a Postgres database. Allows users to post pitches,view pitches and comment on pitches.

### By Esther Muigai

## Setup/Installation Requirements

### Prerequisites
* python3.6
* pip
* Virtual environment(virtualenv)

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In terminal:

  *  $ git clone https://github.com/esthermuigai/news_app/
  *  $ cd news_app

## Creating the virtual environment

  *  $ python3.6 -m venv --without-pip virtual
  *  $ source virtual/bin/env
  *  $ curl https://bootstrap.pypa.io/get-pip.py | python

## Installing Flask and other Modules

  *  Check requirements in requirement.txt


* Run the application:

  *   $ chmod a+x start.sh
  *   $ ./start.sh
## Testing the Application
To run the tests for the class files:

  *  $ python3.6 manage.py test

## Technologies Used
* Python 3.6
* Flask

## Behaviour driven development/ Specifications
| Behaviour    | Input     | Output|
| :------------- | :------------- |:---------|
|  On the site      |  Click Profile   | Redirects to your profile|
|Post a pitch|Click on 'Sumbit'| Posts on timeline and profile|
|Register |Click on register|Get welcome emailon email address provided|


## Support and contact details
Feel free to reach out to the developer at:

* Email: esthermuigaimuthoni@gmail.com
## License
MIT License Copyright (c) {2019} Esther Muigai
