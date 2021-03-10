from rest_framework import serializers
from .models import Company, Advertisement, AdImage


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
        fields = ('company', 'title', 'body', 'created_at', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = instance.images.count()
        representation['company'] = instance.company.company_name
        return representation


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'body',  'company')


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'body', 'created_at', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True).data
        representation['company'] = instance.company.company_name
        return representation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = ('image', 'description', 'id', 'advertisement')