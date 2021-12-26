from rest_framework import status
from rest_framework.response import Response
from .models import CalculatorHistory
from .serializer import CalculatorHistorySerializer
from account.models import Account

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CalculatorHistorySerializer
from .models import CalculatorHistory



class CalculatorHistoryAPIView(APIView):
    serializer_class = CalculatorHistorySerializer
    throttle_scope = "history"
    queryset = CalculatorHistory.objects.all()

    def get_queryset(self):
        history = CalculatorHistory.objects.all()
        return history

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, *args, **kwargs):
        try:
            my_id = request.query_params["id"]
   
            history = CalculatorHistory.objects.filter(author=my_id)
          
            serializer = CalculatorHistorySerializer(history, many=True)
        
        except Exception as e:
      
            history = self.get_queryset()
            serializer = CalculatorHistorySerializer(history, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        serializer = CalculatorHistorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

