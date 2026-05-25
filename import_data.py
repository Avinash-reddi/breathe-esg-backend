import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from ingestion.utils import import_emissions_csv

result = import_emissions_csv('sample_emissions.csv')

print(result)