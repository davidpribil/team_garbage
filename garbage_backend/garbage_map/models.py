from django.contrib.gis.db import models


class ROI(models.Model):
    city_id = models.TextField()
    osm_id = models.TextField()
    cci_id = models.TextField(null=True)
    roi_type = models.TextField()
    geometry = models.TextField()

    polygon = models.PolygonField(null=True)
    line_string = models.LineStringField(null=True)

