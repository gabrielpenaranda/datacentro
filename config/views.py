from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def sistema(request):
	return render(request, 'sistema.html')