import random
from base import Base
from config import DEPARTURE_DATE, DEPARTURE_DATES, SEARCH_TRAIN_URL, SELECT_TRAIN_URL




class TrainPage(Base):

    """
    Course page Class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(TrainPage, self).__init__(*args, **kwargs)

    def search_train(self):
        """
        Search train
        """
        date = random.choice(DEPARTURE_DATES)
        dep_date = '&departure_date={}'.format(date)
        url = SEARCH_TRAIN_URL + dep_date
        self._get(
            url,
            response_string='Successfully fetched available trains' or "Operation successful",
            url_group_name="Search Train"
        )

    def select_train(self):
        """
        Visit Course main page
        """
        dep_date = '&departure_date={}'.format(DEPARTURE_DATE)
        url = SELECT_TRAIN_URL + dep_date
        self._get(
            url,
            response_string='Successfully fetched train coaches',
            url_group_name="Select Train"
        )
