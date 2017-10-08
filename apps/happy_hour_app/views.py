from django.shortcuts import render

def index(request):
    context = {
    'name': 'Tri Tran'
    }
    return render(request, 'happy_hour_app/index.html', context)
# Create your views here.
