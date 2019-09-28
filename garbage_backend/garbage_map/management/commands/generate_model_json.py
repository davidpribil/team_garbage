from django.core.management.base import BaseCommand, CommandError
from garbage_map.model.request_builder import build_model_parameters, build_date_block
import datetime as dt
import json


class Command(BaseCommand):
    help = "Generate some jsons for model"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        date_time_object = dt.datetime.strptime("2019-09-25", "%Y-%m-%d")
        print(json.dumps(build_model_parameters(date_time_object)))
