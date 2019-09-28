from django.contrib.gis.db import models


class ROI(models.Model):
    city_id = models.TextField()
    osm_id = models.TextField()
    cci_id = models.TextField(null=True)
    roi_type = models.TextField()
    geometry = models.TextField()

    polygon = models.PolygonField(null=True)
    line_string = models.LineStringField(null=True)

    class Meta:
        indexes = [models.Index(fields=["osm_id"]), models.Index(fields=["cci_id"])]


class RoiInfo(models.Model):
    collection = models.TextField()
    suitcase_id = models.TextField()
    place_name = models.TextField()
    place_type = models.TextField()
    osm_id = models.TextField()
    cci_id = models.TextField()
    date = models.DateTimeField()
    cci = models.FloatField()
    rateCigarrettes = models.FloatField()
    ratePapers = models.FloatField()
    rateBottles = models.FloatField()
    rateExcrements = models.FloatField()
    rateSyringues = models.FloatField()
    rateGums = models.FloatField()
    rateLeaves = models.FloatField()
    rateGrits = models.FloatField()
    rateGlassDebris = models.FloatField()

    @classmethod
    def find_infos(cls, roi):
        return cls.objects.filter(osm_id=roi.osm_id, cci_id=roi.cci_id).order_by("date")

    @classmethod
    def find_place_type(cls, roi):
        place_type = (
            cls.objects.filter(osm_id=roi.osm_id, cci_id=roi.cci_id)
            .values_list("place_type", flat=True)
            .distinct()
        )
        return place_type[0] if place_type else None

    class Meta:
        indexes = [models.Index(fields=["osm_id"]), models.Index(fields=["cci_id"])]


class Weather(models.Model):
    max_temp = models.FloatField()
    mean_temp = models.FloatField()
    mean_wind_speed = models.FloatField()
    min_temp = models.FloatField()
    total_prep = models.FloatField()
    validdate = models.DateTimeField()


class Event(models.Model):
    lat_long = models.PointField()
    start_time = models.DateTimeField()
    city_name = models.TextField()
    title = models.TextField()
    url = models.URLField()
    venue_name = models.TextField()
    venue_address = models.TextField(null=True)
    postal_code = models.TextField(null=True)
    all_day = models.IntegerField(null=True)
    calendar_count = models.TextField(null=True)
    comment_count = models.TextField(null=True)

