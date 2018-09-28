from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import GenericAPIView

from company.serializers import CompanySerializer, OfficeSerializer, ChangeHeadQuarterSerializer
from company.models import Company, Office


class CompanyListViewSet(ReadOnlyModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class OfficeListViewSet(ReadOnlyModelViewSet):
    serializer_class = OfficeSerializer

    def get_queryset(self):
        pk = self.request.query_params.get('pk')
        return Office.objects.filter(company_id=pk)


class ChangeCompanyHeadQuarter(GenericAPIView):
    serializer_class = ChangeHeadQuarterSerializer
    queryset = Company.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ChangeHeadQuarterSerializer(data=request.data)
        if serializer.is_valid():
            company = Company.objects.get(pk=serializer.validated_data['company_id'])
            company.headquarter_id = serializer.validated_data['headquarter_id']
            company.save()
            return Response(
                data={
                    'message': 'OK'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    'errors': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
