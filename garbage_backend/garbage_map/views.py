from django.http import HttpResponse
from django.template import loader
from garbage_map.models import ROI
import json


def index(request):
    template = loader.get_template("garbage_map/index.html")
    polygons = []
    for roi in ROI.objects.all():
        if roi.geometry == "Polygon":
            points = roi.polygon.coords
        else:
            points = roi.line_string.coords
        polygons.append({"geometry": roi.geometry, "points": json.dumps(points)})
    context = {"polygons": polygons}
    return HttpResponse(template.render(context, request))
