from django.core.management.base import BaseCommand, CommandError
from garbage_map.models import Event
from pathlib import Path
import csv
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = "Populate the event info table"

    def add_arguments(self, parser):
        parser.add_argument("source_csv", type=Path)

    def handle(self, *args, **options):
        with options["source_csv"].open(encoding="utf-8-sig") as fr:
            reader = csv.DictReader(fr)
            objects = []
            for row in reader:
                row["lat_long"] = Point(float(row["latitude"]), float(row["longitude"]))
                del row["latitude"]
                del row["longitude"]
                del row["id"]
                objects.append(Event(**row))
            Event.objects.bulk_create(objects)
