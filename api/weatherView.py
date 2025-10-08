from django.shortcuts import render
# Create your views here.

import requests

API_KEY = "YOUR KEY HERE"

def main(request):
    if request.method=="POST":
        city = request.POST['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            return render(request, 'main.html', {'data': data})
        
        except:
            error = "Search data"
            return render(request, 'index.html', {'error': error})
        
    else:
        return render(request,'main.html')