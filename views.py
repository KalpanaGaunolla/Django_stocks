from django.shortcuts import render, redirect
from .models import stock
from django.contrib import messages
from .forms import Stockform


def home(request):
    import requests
    import json

    if request.method=='POST':
        ticker = request.POST['ticker']    
        api_request = requests.get('https://api.iex.cloud/v1/data/core/quote/'+ticker+'?token=pk_bf4ccf1ec4c44c4d9d919ca522b2f788')
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = 'Error...'
        return render(request,'home.html',{'api':api[0]})

    else:
        return render(request,'home.html',{'ticker':'Enter a ticker symbol above..'})
    #pk_bf4ccf1ec4c44c4d9d919ca522b2f788
    

def about(request):
    return render(request,'about.html',{})

def add_stock(request):
     import requests
     import json

     if request.method == 'POST':
        form = Stockform(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,('Stcok has been added'))
            return redirect('add_stock')
    
     else:
        ticker = stock.objects.all()
        output = []

        for ticker_item in ticker:
            
            api_request = requests.get('https://api.iex.cloud/v1/data/core/quote/'+str(ticker_item)+'?token=pk_bf4ccf1ec4c44c4d9d919ca522b2f788')
            
            try:
                api = json.loads(api_request.content)
                output.append(api[0])
            except Exception as e:
                api = 'Error...'
     return render(request,'add_stock.html',{'ticker':ticker,'output':output})

def delete(request,stock_id):
    item = stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,('Stock has been deleted'))

    return redirect(delete_stock)

def delete_stock(request):
    
    ticker = stock.objects.all()
    return render(request,'delete_stock.html',{'ticker':ticker})