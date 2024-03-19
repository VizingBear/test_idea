from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def test_view(request):
    # return HttpResponse('./test.html')
    return render(request, 'test.html')

def test_view_final(request):
    first_date=request.POST['first_date']
    last_date=request.POST['last_date']
    return render(request, 'test2.html', {'first_date':first_date, 'last_date':last_date})

