from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from company.views import CompanyListViewSet, OfficeListViewSet, ChangeCompanyHeadQuarter


router = DefaultRouter()
router.register(r'companies', CompanyListViewSet, base_name='company')
router.register(r'company/offices', OfficeListViewSet, base_name='office')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'company/update_headquarter/', ChangeCompanyHeadQuarter.as_view(), name='update_headquarter'),
    url(r'^', include(router.urls))
]