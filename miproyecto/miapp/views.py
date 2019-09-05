from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')
def formulario(request):
	return render(request, 'miapp/formulario.html')
def chrono(request):
	return render(request, 'miapp/chrono.html')