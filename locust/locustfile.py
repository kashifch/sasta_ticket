import os
from locust import HttpLocust, TaskSet
from TrainLocustTasks import SearchTrainsTasks, SelectTrainsTasks


class TrainTasks(TaskSet):
    """
    Execute Load tests
    """
    tasks = {

        SearchTrainsTasks: 10,
        SelectTrainsTasks: 1
    }


class ArbisoftLocust(HttpLocust):
    """
    Representation of an HTTP "user".
    Defines how long a simulated user should wait between executing tasks, as
    well as which TaskSet class should define the user's behavior.
    """
    task_set = globals()[os.getenv('TASK_SET', 'TrainTasks')]
    min_wait = 20000
    max_wait = 50000