import datetime as dt
from garbage_map.models import Event, Weather, ROI, RoiInfo


def build_model_parameters(date_to_predict):
    result = []
    for date in [date_to_predict - dt.timedelta(i) for i in range(3)]:
        result += build_date_block(date)
    return result


def build_date_block(date):
    # Prepare data not depending on ROI
    weather_for_the_day = Weather.objects.filter(validdate=date)
    if weather_for_the_day.count() != 1:
        raise Exception("No date, or more than one date for input date")
    weather_for_the_day = weather_for_the_day[0]
    events_for_the_day = Event.objects.filter(start_time__date=date)
    day_of_the_week = date.strftime("%A")

    result = []
    # Generate response for ROI
    for roi in ROI.objects.all():
        place_type = RoiInfo.find_place_type(roi)
        if roi.geometry == "Polygon":
            points = roi.polygon.coords
        else:
            points = roi.line_string.coords
        result.append(
            {
                "date": date.strftime("%Y-%m-%d"),
                "day_of_week": day_of_the_week,
                "osm_id": roi.osm_id,
                "cci_id": roi.cci_id,
                "geometry": roi.geometry,
                "coords": points,
                "place_type": place_type,
                "weather": {
                    "min": weather_for_the_day.min_temp,
                    "max": weather_for_the_day.max_temp,
                    "mean": weather_for_the_day.mean_temp,
                    "precipitation": weather_for_the_day.total_prep,
                    "wind": weather_for_the_day.mean_wind_speed,
                },
                "events": [ev.lat_long.coords for ev in events_for_the_day],
            }
        )
    return result
