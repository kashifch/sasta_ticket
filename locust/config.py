# Constants and URLS
import os

# Environment variables for Both APIs
ORIGIN = os.getenv("ORIGIN", "LHR")
DESTINATION = os.getenv("DESTINATION", "KC")
DEPARTURE_DATE = os.getenv("DEPARTURE_DATE", "2017-08-23")
NUM_ADULT = os.getenv("NUM_ADULT", "1")
NUM_CHILD = os.getenv("NUM_CHILD", "0")


# Environment variables for Select API
TRAIN = os.getenv("TRAIN", "45")
CLASS_CODE = os.getenv("CLASS_CODE", "EC")
UNIT_FARE = os.getenv("UNIT_FARE", "1160")
WEB_REFERENCE = os.getenv("WEB_REFERENCE", "TRN-0000707")


SEARCH_TRAIN_URL = u"/api/train/v1/get_available_trains/?origin={}&destination={}&departure_date={}&num_adult={}&num_child={}".format(
    ORIGIN,
    DESTINATION,
    DEPARTURE_DATE,
    NUM_ADULT,
    NUM_CHILD
)

SELECT_TRAIN_URL = u"/api//train/v1/get_train_coaches/?train={}&origin={}&destination={}&departure_date={}&num_adult={}&num_child={}&class_code={}&unit_fare={}&web_reference={}".format(
    TRAIN,
    ORIGIN,
    DESTINATION,
    DEPARTURE_DATE,
    NUM_ADULT,
    NUM_CHILD,
    CLASS_CODE,
    UNIT_FARE,
    WEB_REFERENCE
)
