from django.db.models.base import Model
from rest_framework import serializers
from .models import CalculatorHistory

class CalculatorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatorHistory
        fields = '__all__' 