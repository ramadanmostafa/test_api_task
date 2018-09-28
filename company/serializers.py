from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Company, Office


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'street', 'postal_code', 'city', 'total_rent')


class OfficeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Office
        fields = ("id", "street", "postal_code", "city", "monthly_rent")


class ChangeHeadQuarterSerializer(serializers.HyperlinkedModelSerializer):
    headquarter_id = serializers.IntegerField(required=True)
    company_id = serializers.IntegerField(required=True)

    def validate(self, data):
        try:
            company = Company.objects.get(id=data['company_id'])
        except Company.DoesNotExist:
            raise ValidationError({'company_id': "company not found"})
        try:
            company.offices.get(pk=data['headquarter_id'])
        except Office.DoesNotExist:
            raise ValidationError({'headquarter_id': "office not found"})
        return data

    class Meta:
        model = Company
        fields = ('company_id', 'headquarter_id')