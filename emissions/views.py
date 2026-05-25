from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord
from .serializers import EmissionRecordSerializer


@api_view(['GET'])
def emission_list(request):
    emissions = EmissionRecord.objects.all()
    serializer = EmissionRecordSerializer(emissions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def esg_score(request):

    emissions = EmissionRecord.objects.all()

    total_score = []

    for emission in emissions:

        score = (
            emission.renewable_energy_percentage
            - (emission.scope1_emissions * 0.1)
            - (emission.scope2_emissions * 0.05)
            - (emission.scope3_emissions * 0.01)
        )

        total_score.append({
            "company": emission.company.name,
            "year": emission.year,
            "esg_score": round(score, 2)
        })

    return Response(total_score)