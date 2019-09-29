from django.http import HttpResponse, JsonResponse
from django.template import loader
from garbage_map.models import ROI, RoiInfo, Event
import json
from dateutil import parser
from garbage_map.model.request_builder import get_predictions


def index(request):
    template = loader.get_template("garbage_map/index.html")
    polygons = []
    for roi in ROI.objects.all()[:5]:
        if roi.geometry == "Polygon":
            points = roi.polygon.coords
        else:
            points = roi.line_string.coords
        polygons.append(
            {"geometry": roi.geometry, "points": json.dumps(points), "osm": roi.osm_id}
        )
    context = {"polygons": polygons}
    return HttpResponse(template.render(context, request))


def calc_results(request):
    """
    < 3 red
    >= 3 and < 4 yellow
    >= 4 green
    """
    date = parser.parse(request.GET["date"]).date()
    # We either display things in prediction or historical data mode
    matching_roi = RoiInfo.objects.filter(date__date=date)
    predictions = {}
    if not matching_roi:
        # Prediction. Get all ROIs and predictions for the date
        roi_data, prediction_array = get_predictions(date)
        for idx, roi_datum in enumerate(roi_data):
            prediction = prediction_array[idx]
            clazz = get_class(prediction)
            predictions[f"{roi_datum['osm_id']}_{roi_datum['cci_id']}"] = {
                "class": clazz,
                "cont": prediction,
            }
        pred_label = "Prediction"
    else:
        roi_infos = RoiInfo.objects.filter(date__date=date)
        for ri in roi_infos:
            cci = ri.cci
            clazz = get_class(cci)
            predictions[f"{ri.osm_id}_{ri.cci_id}"] = {"class": clazz, "cont": cci}
        pred_label = "Historical Data"
    results = []
    events_for_the_day = Event.objects.filter(start_time__date=date)
    event_names = [f"{e.title} - {e.venue_name}" for e in events_for_the_day]
    for key, value in predictions.items():
        split = key.split("_", 1)
        osm = split[0]
        cci = split[1]
        if cci == "nan":
            cci = "NA"
        roi = ROI.objects.get(osm_id=osm, cci_id=cci)
        points = get_roi_points(roi)
        clazz = value["class"]
        raw_score = value["cont"]
        if clazz == 0:
            color = "red"
        elif clazz == 1:
            color = "yellow"
        else:
            color = "green"
        place_name = RoiInfo.find_place_name(roi)
        place_type = RoiInfo.find_place_type(roi)
        poly = roi.polygon if roi.geometry == "Polygon" else roi.line_string
        popup_content = [place_name, place_type]
        results.append(
            {
                "geometry": roi.geometry,
                "points": points,
                "color": color,
                "popupContent": popup_content,
            }
        )
    return JsonResponse(
        {"rois": results, "events": event_names, "prediction": pred_label}, safe=False
    )


def get_class(prediction):
    if prediction < 3:
        clazz = 0
    elif prediction < 4:
        clazz = 1
    else:
        clazz = 2
    return clazz


def get_roi_points(roi):
    if roi.geometry == "Polygon":
        points = roi.polygon.coords
    else:
        points = roi.line_string.coords
    return points
