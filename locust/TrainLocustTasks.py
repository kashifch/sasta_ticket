from locust import task, TaskSet
from train import TrainPage


class SearchTrainsTasks(TaskSet):
    """
    User scripts that tests the login
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(SearchTrainsTasks, self).__init__(*args, **kwargs)
        self.train = TrainPage(self.locust.host, self.client)

    @task(1)
    def search_train(self):
        """
        View the pages repeatedly
        """
        self.train.search_train()


class SelectTrainsTasks(TaskSet):
    """
    User scripts that tests the login
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(SelectTrainsTasks, self).__init__(*args, **kwargs)
        self.train = TrainPage(self.locust.host, self.client)

    @task(1)
    def select_train(self):
        """
        View the pages repeatedly
        """
        self.train.select_train()
