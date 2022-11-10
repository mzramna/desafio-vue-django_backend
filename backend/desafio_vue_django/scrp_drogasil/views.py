from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from scrp_drogasil.serializers import PesquisaSerializer
from scrp_drogasil.scrap import pesquisa
@csrf_exempt
def pesquisaAPI(request):
    if request.method in ['GET','PUT','DELETE']:
        JsonResponse('INVALID METHOD',safe=False)
    elif request.method=='POST':
        produtos=JSONParser().parse(request)
        pesquisa_serializer=PesquisaSerializer(data=produtos)
        if pesquisa_serializer.is_valid():
            if 'quantidade' in  produtos.keys():
                retorno= JsonResponse(pesquisa.query_quantidade(palavrasChave=produtos["palavrasChave"],quantidade=produtos['quantidade']),safe=False)
            else:
                retorno= JsonResponse(pesquisa.query_quantidade(palavrasChave=produtos["palavrasChave"]),safe=False)
            retorno["Access-Control-Allow-Origin"] = "*"
            retorno["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            retorno["Access-Control-Max-Age"] = "1000"
            retorno["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return retorno