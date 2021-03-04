from rest_framework import generics, status
from rest_framework.response import Response

from .models import Company, Advertisement
from .pagination import ListPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (CompanySerializer, CompanyCreateSerializer,
                          CompanyDetailSerializer, AdvertisementSerializer,
                          AdvertisementCreateSerializer, AdvertisementDetailSerializer)


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


class AdView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pagination_class = ListPagination
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('company__company_name', 'title')
    search_fields = ('company__company_name', 'title')


class AdCreate(generics.CreateAPIView):
    serializer_class = AdvertisementCreateSerializer

    def create(self, request, *args, **kwargs):
        print('REQUEST DATA', request.data)
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['company'])
        print(company.owner)
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            print(serializer.data)
            headers = self.get_success_headers(serializer.data)
            return Response({"OK"}, status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            return Response({'You do not have permissions'},
                            status=status.HTTP_400_BAD_REQUEST)


class AdDetail(generics.RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer
