import json
from base import Base
from config import SEARCH_FLIGHT_URL


class FlightPage(Base):

    """
    Course page Class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(FlightPage, self).__init__(*args, **kwargs)

    def search_flight(self, ddate, orig, dest, adults, child, infant):
        """
        Search train
        """
        url = SEARCH_FLIGHT_URL
        default_headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=utf-8'
        }

        params = {'arrivalDate': None,'cabin_type':'Y','departureDate':ddate,'destination':dest,'flexibility':None,'non_stop_flight':'false','num_adult':adults,'num_child':child,'num_infant':infant ,'origin':orig,'trip_type':'ONEWAY','trips':[{'origin':orig,'destination':dest,'departure_date':ddate}]}
        r = self.client.post(url=url, headers=default_headers, data=json.dumps(params), verify=False)
        self._check_response(r)
        return r



