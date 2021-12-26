
from django.db import models
from account import models as account_models

# Create your models here.
class CalculatorHistory(models.Model):
    expression = models.CharField(max_length=300)
    result = models.CharField(max_length=300)
    author = models.ForeignKey(account_models.Account,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.expression)+" = "+str(self.result)
