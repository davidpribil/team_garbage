from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("garbage_map/index.html")
    context = {"trash": "total_trash"}
    return HttpResponse(template.render(context, request))
