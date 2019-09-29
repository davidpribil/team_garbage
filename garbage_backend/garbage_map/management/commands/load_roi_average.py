from django.core.management.base import BaseCommand, CommandError
from garbage_map.models import ROI
from pathlib import Path
import csv


class Command(BaseCommand):
    help = "Add averages to ROI table"

    def add_arguments(self, parser):
        parser.add_argument("source_csv", type=Path)

    def handle(self, *args, **options):
        with options["source_csv"].open() as fr:
            reader = csv.DictReader(fr)
            for row in reader:
                rois = ROI.objects.filter(osm_id=row["osm_id"], cci_id=row["cci_id"])
                for roi in rois:
                    roi.average = row["average"]
                    roi.save()

