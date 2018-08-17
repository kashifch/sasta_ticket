Locust Tests
---------------

The tests in this directory utilize the [Locust](http://docs.locust.io/en/latest/) load testing tool.

Getting Started
---------------
Get started by first installing Locust and any other prerequisites using the below command (optionally you could 
create a virtual env before installing the software)  

    $ pip install -r requirements.txt

The locust folder contains a `locustfile.py`. In order to run the tests, cd into the locust folder and run the 
`locust` command as shown below. Remember to replace `<host>` with the hostname of the actual server being tested.

    $ locust --host=<host>
Example:  
 
    $ locust --host=http://site_name
    
The Tasks are mainly divided in two Parts, the SearchTrainsTasks and the SelectTrainsTasks. By default both task will run simultaneously.

To run these tasks seperately you can specify a single task in command

    $ TASK_SET=SearchTrainsTasks locust --host=http://site_name
    $ TASK_SET=SelectTrainsTasks locust --host=http://site_name
    
After running the command visit `http://127.0.0.1:8089` and provide number of users and hatch rate (how many 
users to add per second)


To Run Train Tests
-------------------


There are a number of Optional Environment Variables that you can use to change the API URLS

These are 

##### Environment variables for Both APIs
ORIGIN -- City of Origin, default value is LHR
DESTINATION -- Destination, default value is KC
DEPARTURE_DATE = Departure Date, default value is "2017-08-23"
NUM_ADULT = Number of Adults, default value is 1
NUM_CHILD = Number of Children, default value is 0

##### Environment variables for Select API
TRAIN -- ID of train, default value is 45
CLASS_CODE = Class Code, default value is EC
UNIT_FARE = Unit Fare, default value is 1160
WEB_REFERENCE = Web Reference of serached Train, default value is TRN-0000707

###### Example

Following Example uses different values for Train, Unit Fare, Web Refrence and run only the Select Train Task

    $TASK_SET=SelectTrainsTasks, TRAIN=60, UNIT_FARE=1290, WEB_REFERENCE=TRN-000897 locust --host=htts://Site-name
    
    
    
To Run Flight Tests
-------------------

Flight Test is set as default and there is no environment var involved so it can be run directly using

    $ locust --host=http://site_name

Just change the DATE_RANGE_START and DATE_RANGE_END values in config files, the script will get a random
date between this range for each user


