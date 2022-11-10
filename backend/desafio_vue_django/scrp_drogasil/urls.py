from django.urls import re_path
from scrp_drogasil import views

urlpatterns = [
    re_path(r"^pesquisa/", views.pesquisaAPI, name="pesquisaApi"),
]
