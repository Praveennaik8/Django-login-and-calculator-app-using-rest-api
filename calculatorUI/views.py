from django.shortcuts import redirect, render
from calculatorUI.calculate import Solution
import requests

URL = 'http://127.0.0.1:8000/api/history/'
    
def calculator(request):
    result = ""
    user = request.user
    if user.is_authenticated: 
        if request.POST:
            expression = request.POST['result']
            result = Solution.calculate(expression)
            if result != 'Nan':
                data = {
                    'expression':expression,
                    'result':result,
                    'author':user.id
                }
                response = requests.post(URL,data=data)
                if not (response.status_code == 200 or response.status_code == 201):
                    result = str(result)
                    result+="/n "+"Error while saving record"
                
        return render(request,'calculatorUI/calculator.html',{'result':result})
    
    return redirect("/login")

def history(request):
    
    response = requests.get(URL,params={'id': request.user.id})
    
    try:
        extracted = response.json()
        
        results = {}
    
        if not isinstance(extracted, list):
            extracted = [extracted]
        for item in extracted:
            results[item['expression']] = item['result']
    except:
        results={'No expression':''}
    return render(request,'calculatorUI/history.html',{'result':results})