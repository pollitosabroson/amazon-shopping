import csv
import logging

from flask import Blueprint
from manager.amz_manager import AmzManager
from slugify import slugify

# Create a custom logger
logger = logging.getLogger(__name__)

commands = Blueprint('import', __name__)


def parse_value(value):
    """Conver value in to float or str."""
    try:
        return float(value)
    except ValueError:
        return value


@commands.cli.command('amz')
def create():
    # TODO Open and name Dynamic
    with open('/app/shared/Retail.OrderHistory.csv', mode='r', encoding='utf-8-sig') as csv_file:  # NOQA

        data = []
        for line in csv.DictReader(csv_file):
            data.append(
                {
                    slugify(k, separator="_"): parse_value(v)
                    for k, v in line.items()
                }
            )

        AmzManager.insert_many(data=data)
