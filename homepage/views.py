from django.shortcuts import render

def main(request):
    return render(request, 'homepage/main.html')

def food(request):
    return render(request, 'homepage/food.html')
def fashion(request):
    return render(request, 'homepage/fashion.html')

def delivery(request):
    return render(request, 'homepage/delivery.html')

# Create your views here.
