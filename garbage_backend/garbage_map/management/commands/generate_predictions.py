from django.core.management.base import BaseCommand, CommandError
from garbage_map.model.request_builder import get_predictions
import datetime as dt
import csv

challenge_dates = [
    "2019-06-25",
    "2019-06-26",
    "2019-06-27",
    "2019-06-28",
    "2019-08-28",
    "2019-08-29",
    "2019-08-30",
    "2019-08-31",
    "2019-09-21",
    "2019-09-22",
    "2019-09-23",
    "2019-09-24",
]


class Command(BaseCommand):
    help = "Generate some jsons for model"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for date in challenge_dates:
            date_time_object = dt.datetime.strptime(date, "%Y-%m-%d")
            roi_data, predictions = get_predictions(date_time_object)
            with open(f"results/challenge_{date}.csv", "w") as fw:
                writer = csv.DictWriter(
                    fw, fieldnames=["osm_id", "cci_id", "prediction"]
                )
                writer.writeheader()
                for idx, roi_datum in enumerate(roi_data):
                    pred = predictions[idx]
                    writer.writerow(
                        {
                            "osm_id": roi_datum["osm_id"],
                            "cci_id": roi_datum["cci_id"],
                            "prediction": pred,
                        }
                    )
