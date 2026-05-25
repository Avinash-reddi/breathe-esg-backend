import pandas as pd

from companies.models import Company
from emissions.models import EmissionRecord


def import_emissions_csv(file_path):

    data = pd.read_csv(file_path)

    for _, row in data.iterrows():

        company, created = Company.objects.get_or_create(
            name=row['company'],
            defaults={
                'industry': row['industry'],
                'headquarters': row['headquarters'],
                'total_employees': row['employees']
            }
        )

        EmissionRecord.objects.create(
            company=company,
            year=row['year'],
            scope1_emissions=row['scope1'],
            scope2_emissions=row['scope2'],
            scope3_emissions=row['scope3'],
            renewable_energy_percentage=row['renewable_percentage']
        )

    return "CSV Imported Successfully"