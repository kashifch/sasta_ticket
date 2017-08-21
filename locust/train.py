from base import TrainBase
from config import SEARCH_TRAIN_URL, SELECT_TRAIN_URL


class TrainPage(TrainBase):

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
        self._get(
            SEARCH_TRAIN_URL,
            response_string='Successfully fetched available trains',
            url_group_name="Searh Train"
        )

    def select_train(self):
        """
        Visit Course main page
        """
        self._get(
            SELECT_TRAIN_URL,
            response_string='Successfully fetched train coaches',
            url_group_name="Select Train"
        )
