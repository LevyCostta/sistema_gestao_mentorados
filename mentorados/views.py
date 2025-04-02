from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mentorados(request):
    if request.method == 'GET':
        return render(request, 'mentorados.html')