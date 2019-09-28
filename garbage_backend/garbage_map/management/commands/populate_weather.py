from django.core.management.base import BaseCommand, CommandError
from garbage_map.models import Weather
from pathlib import Path
import csv


class Command(BaseCommand):
    help = "Populate the weather info table"

    def add_arguments(self, parser):
        parser.add_argument("source_csv", type=Path)

    def handle(self, *args, **options):
        with options["source_csv"].open(encoding="utf-8-sig") as fr:
            reader = csv.DictReader(fr)
            objects = []
            for row in reader:
                objects.append(Weather(**row))
            Weather.objects.bulk_create(objects)
