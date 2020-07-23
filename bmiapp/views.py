from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def result(request):
    height = float(request.POST['height'])/100
    weight = float(request.POST['weight'])
    result = round(weight / (height ** 2), 1)
    if result < 18.5:
        status = 'UNDER WEIGHT'
    elif result >= 18.5 and result <= 24.9:
        status = 'NORMAL'
    elif result >= 25 and result <= 29.9:
        status = 'OVER WEIGHT'
    elif result >= 30 and result <= 34.9:
        status = 'OBESE'
    else:
        status = 'EXTREMLY OBSESE'

    return render(request, 'result.html', {'result': result, 'status': status, 'height': height * 100, 'weight': weight})
