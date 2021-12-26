from rest_framework import viewsets
from . import models
from . import serializer

class HistoryViewset(viewsets.ModelViewSet):
    queryset = models.CalculatorHistory.objects.all()
    serializer_class = serializer.CalculatorHistorySerializer