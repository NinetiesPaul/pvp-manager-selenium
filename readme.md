## pvp-manager-selenium
This is a repository with selenium automoted tests to validate the features of the https://github.com/NinetiesPaul/pvp-manager

### Set up
We will be using docker containers running selenium to perform the tests, so Docker container should be good to go on your enviroment.

Once Docker is instaled run:
```
docker-compose build
```
To build the selenium container. Once this is completed run:
```
docker-compose up -d
```
To run the container itself and set Selenium ready to run tests.
The tests are written in Python and as such you must have Python itself configured on your enviroment, as this project doesn't have a Python container.

### Running tests
The tests itself are written in Python, and for now there is no container running Python on this project, which means you should have Python installed and configured on your enviroment.

Once Python is ready, to perform a test you can either:

### 1) Run all tests
Just run:
```
python run_test.py
```
To perform all the tests available; or you can

### 2) Run specific test
For this use:
```
python run_test.py TestName
```
And the script will carry out that specific test.