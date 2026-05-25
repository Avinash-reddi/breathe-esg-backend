from django.db import models
from companies.models import Company


class EmissionRecord(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()

    scope1_emissions = models.FloatField()
    scope2_emissions = models.FloatField()
    scope3_emissions = models.FloatField()

    renewable_energy_percentage = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.year}"