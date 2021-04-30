from django.shortcuts import render

from .models import *


def index(request):
	itemGroups = itemGroup.objects.all()
	context = {'itemGroups': itemGroups}

	return render(request, 'index.html', context)