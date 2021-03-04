from rest_framework import serializers
from .models import Company, Advertisement


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'info', 'id')


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'logo', 'address', 'phone', 'info')

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validated_data)
        company.save()
        return company


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('owner', 'company_name', 'logo', 'address', 'phone', 'info', 'id')


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'image', 'created_at', 'id')


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'body', 'image', 'company')


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'image', 'created_at', 'id')