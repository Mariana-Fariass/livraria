from livraria.models.livro import Livro
from livraria.serializers import LivroDetailSerializer, LivroListSerializer, LivroSerializer
from rest_framework.viewsets import ModelViewSet


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer