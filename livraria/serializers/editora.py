from livraria.models.editora import Editora
from rest_framework.serializers import ModelSerializer


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"