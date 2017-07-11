from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'default/index.html')

def landscape(request, number):
    num = int(number)
    if num >= 1 and num <= 10:
        backdrop = 'snow'
    elif num >= 11 and num <= 20:
        backdrop = 'desert'
    elif num >= 21 and num <= 30:
        backdrop = 'forest'
    elif num >= 31 and num <= 40:
        backdrop = 'vineyard'
    elif num >= 41 and num <= 50:
        backdrop = 'tropical'
    request.session['landscape'] = backdrop
    print request.session['landscape']
    return render(request, 'default/landscape.html')
