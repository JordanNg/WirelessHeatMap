from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from scripts.helpers import Building_Helper
import scripts.pull_airwave as PA
import airwaveapiclient
from influxdb import InfluxDBClient
import time
import xmltodict
import os

BASE_DIR = settings.BASE_DIR
LOCAL_DIR = os.path.dirname(__file__)

BH = Building_Helper

class Command(BaseCommand):
    help = 'Pulls data from airwave'
    
    def handle(self, *args, **options):
        PA.pull_data()
