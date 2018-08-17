# Constants and URLS
import os
import datetime

# Environment variables for Both APIs
ORIGIN = os.environ.get("ORIGIN", "LHR")
DESTINATION = os.environ.get("DESTINATION", "KC")
NUM_ADULT = os.environ.get("NUM_ADULT", "1")
NUM_CHILD = os.environ.get("NUM_CHILD", "0")
DEPARTURE_DATE = os.environ.get("DAPARTURE_DATE", "2017-10-23")

base = datetime.datetime.today()
DEPARTURE_DATES = [str((base + datetime.timedelta(days=x)).date()) for x in range(2, 28)]

# Environment variables for Select API
TRAIN = os.environ.get("TRAIN", "45")
CLASS_CODE = os.environ.get("CLASS_CODE", "EC")
UNIT_FARE = os.environ.get("UNIT_FARE", "1100")
WEB_REFERENCE = os.environ.get("WEB_REFERENCE", "TRN-0000136")


SEARCH_TRAIN_URL = u"/api/v1/train/get_available_trains/?origin={origin}&destination={dest}&num_adult={num_adult}&num_child={num_child}".format(
    origin=ORIGIN,
    dest=DESTINATION,
    num_adult=NUM_ADULT,
    num_child=NUM_CHILD
)

SELECT_TRAIN_URL = u"/api/v1/train/get_train_coaches/?train={}&origin={}&destination={}&num_adult={}&num_child={}&class_code={}&unit_fare={}&web_reference={}".format(
    TRAIN,
    ORIGIN,
    DESTINATION,
    NUM_ADULT,
    NUM_CHILD,
    CLASS_CODE,
    UNIT_FARE,
    WEB_REFERENCE
)


SEARCH_FLIGHT_URL = u"/api/v1/flights/get_available_flights/"

DATE_RANGE_START = "2018-08-20"

DATE_RANGE_END = "2018-09-20"
