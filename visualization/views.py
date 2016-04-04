from django.shortcuts import render

# Create your views here.

def panel_test(request):
	return render(request, 'panel/index.html', {})