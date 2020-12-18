from django.shortcuts import render, HttpResponse #response para pruebas

# Create your views here.

def home(request):
	
	#return HttpResponse("home")
	return render(request, "proyectoWebApp/home.html")

def servicios(request):
	
	#return HttpResponse("servicios")
	return render(request, "proyectoWebApp/servicios.html")


def tienda(request):
	
	#return HttpResponse("tienda")
	return render(request, "proyectoWebApp/tienda.html")


def blog(request):
	
	#return HttpResponse("blog")
	return render(request, "proyectoWebApp/blog.html")


def contacto(request):
	
	#return HttpResponse("contacto")
	return render(request, "proyectoWebApp/contacto.html")




