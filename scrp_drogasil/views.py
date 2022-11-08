from django.shortcuts import render
from django.views.decorators import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from scrp_drogasil.serializers import PesquisaSerializer

@csrf_exempt
def pesquisaAPI(request,):
    if request.method=='GET':
        pass
    elif request.method=='POST':
        pass