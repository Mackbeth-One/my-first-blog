# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(response):
	return HttpResponse("Prosta ankieta")
