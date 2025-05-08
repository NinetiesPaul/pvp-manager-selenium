## pvp-manager-selenium
This is a repository with selenium automoted tests to validate the features of the https://github.com/NinetiesPaul/pvp-manager

### Set up
Selenium will be running on a docker container, so you should have Docker installed and ready to be used on your environment.

Once Docker is instaled, run:
```
docker-compose build
```
To build the Selenium container.

Once this is completed:
```
docker-compose up -d
```
To run the container and start Selenium to run tests.
The tests are written in Python and as such you must have it configured on your environment, as this project doesn't have a container running Python.

### Running tests
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