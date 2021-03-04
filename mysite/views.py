from rest_framework import generics
from .models import Company
from .pagination import ListPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (CompanySerializer,
                          CompanyCreateSerializer,
                          CompanyDetailSerializer)


class CompanyView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = ListPagination
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('company_name', 'address', 'owner__username')
    search_fields = ('company_name', 'address', 'owner__username')


class CompanyCreate(generics.CreateAPIView):
    serializer_class = CompanyCreateSerializer

    def get_serializer_context(self):
        context = super(CompanyCreate, self).get_serializer_context()
        context.update({
            'owner': self.request.user
        })
        return context


class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer

