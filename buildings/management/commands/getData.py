from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from buildings.models import Location, Building, Floor, Room
from scripts.helpers import Building_Helper
import logging
import os
import json
    
BASE_DIR = settings.BASE_DIR
LOCAL_DIR = os.path.dirname(__file__)

class Command(BaseCommand):
    help = 'Pulls data for creating the map.'
    def add_arguments(self, parser):
        parser.add_argument('--bandwidth', action='store_true', help='Gets bandwidth usage instead of number of clients')
    def handle(self, *args, **options):
        if options['room']:


