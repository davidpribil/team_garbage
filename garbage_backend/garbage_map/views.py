from django.http import HttpResponse
from django.template import loader
from garbage_map.models import ROI
import json


def index(request):
    template = loader.get_template("garbage_map/index.html")
    context = {"polygon": json.dumps(ROI.objects.first().polygon.coords)}
    return HttpResponse(template.render(context, request))
