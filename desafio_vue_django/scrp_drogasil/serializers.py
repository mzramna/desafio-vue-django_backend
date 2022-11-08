from rest_framework import serializers

class PesquisaSerializer(serializers.Serializer):
    palavrasChave=serializers.CharField(required=True,max_length=200)
    quantidade=serializers.IntegerField(required=False)
    class Meta:
        fields=('palavrasChave','quantidade')
    def get_validation_exclusions(self):
        exclusions = super(FavoriteListSerializer, self).get_validation_exclusions()
        return exclusions + ['quantidade']