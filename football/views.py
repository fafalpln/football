from django.shortcuts import render

def klasyfikacja(request):
	return render(request, 'football/klasyfikacja.html', {})