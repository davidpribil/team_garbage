import datetime as dt
from garbage_map.models import Weather, ROI
import pickle
import numpy as np

# Load the model during init, so avoid excessive I/O
filename = "finalized_model.sav"
rf = pickle.load(open(filename, "rb"))

"""
Model expects:
[
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    "mean_temp",
    "total_prep",
    "latitudes",
    "longitudes",
    "event",
    "year",
    "month",
    "day",
    "average",
]
"""


def get_predictions(date):
    # Prepare data not depending on ROI
    weather_for_the_day = Weather.objects.filter(validdate__date=date)
    if weather_for_the_day.count() != 1:
        raise Exception("No date, or more than one date for input date")
    weather_for_the_day = weather_for_the_day[0]
    # events_for_the_day = Event.objects.filter(start_time__date=date)
    day_of_week = [0 for _ in range(7)]
    day_of_week[date.weekday()] = 1

    params = []
    roi_data = []
    # Generate response for ROI
    for roi in ROI.objects.all():
        if roi.geometry == "Polygon":
            center = roi.polygon.centroid
        else:
            center = roi.line_string.centroid
        params.append(
            [
                *day_of_week,
                weather_for_the_day.mean_temp,
                weather_for_the_day.total_prep,
                center.x,
                center.y,
                0,
                date.year,
                date.month,
                date.day,
                roi.average,
            ]
        )
        roi_data.append({"osm_id": roi.osm_id, "cci_id": roi.cci_id})
    result = rf.predict(params)
    return roi_data, result
