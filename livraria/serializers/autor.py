from livraria.models.autor import Autor
from rest_framework.serializers import ModelSerializer


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
