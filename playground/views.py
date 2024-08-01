from django.shortcuts import render
from .models import Address


def users(request):
    query = Address.objects.select_related('user').all()
    return render(request, 'index.html', {'query': list(query)})
