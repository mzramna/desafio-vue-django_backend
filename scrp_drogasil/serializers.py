from rest_framework import serializers

class PesquisaSerializer(serializers.Serializer):
    class Meta:
        fields=('pesquisa')