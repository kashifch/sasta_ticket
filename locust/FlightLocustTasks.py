import random
import time

from locust import task, TaskSet

from config import DATE_RANGE_START, DATE_RANGE_END
from flight import FlightPage


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


class SearchFlightTasks(TaskSet):
    """
    User scripts that tests the login
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(SearchFlightTasks, self).__init__(*args, **kwargs)
        self.flight = FlightPage(self.locust.host, self.client)
        data = {
            "origin": ["LHE", "ISB", "KHI"],
            "destination": ["DXB", "LHR", "JFK", "VKO", "NRT", "BNE", "MUX", "SYD"],
            "adults": ["1", "2", "3"],
            "child": ["0", "1"],
            "infant": ["0", "1"]
        }
        self.ddate = random_date(DATE_RANGE_START, DATE_RANGE_END, random.random())
        self.orig = random.choice(data["origin"])
        self.dest = random.choice(data["destination"])
        self.num_adults = random.choice(data["adults"])
        self.num_child = random.choice(data["child"])
        self.num_infant = random.choice(data["infant"])

    @task(1)
    def search_train(self):
        """
        View the pages repeatedly
        """

        flag = False
        while flag is False:
            response = self.flight.search_flight(
                self.ddate,
                self.orig,
                self.dest,
                self.num_adults,
                self.num_child,
                self.num_infant
            )
            if "Operation successful" in response.content and "poll" not in response.content:
                flag = True
