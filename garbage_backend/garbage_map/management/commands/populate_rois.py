from django.core.management.base import BaseCommand, CommandError
from garbage_map.models import ROI
from pathlib import Path
import csv


def read_roi(row):
    row["roi_type"] = row["type"]
    del row["type"]
    if row["geometry"] == "Polygon":
        row["polygon"] = row["coordinates"]
    elif row["geometry"] == "LineString":
        row["line_string"] = row["coordinates"]
    else:
        raise CommandError(f"Unkown geometry: {row['geometry']}")
    del row["coordinates"]
    ROI.objects.create(**row)


class Command(BaseCommand):
    help = "Populate the ROI table"

    def add_arguments(self, parser):
        parser.add_argument("source_csv", type=Path)

    def handle(self, *args, **options):
        with options["source_csv"].open() as fr:
            reader = csv.DictReader(fr)
            for row in reader:
                read_roi(row)

