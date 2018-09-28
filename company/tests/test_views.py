from django.urls import reverse
from rest_framework.test import APITestCase

from company.tests.helpers import CompanyTestMixin


class TestCompanyListViewSet(APITestCase, CompanyTestMixin):

    def setUp(self):
        self.setup_companies()

    def test_list(self):
        data = [
            {
                'city': 'Cairo', 'id': self.company.pk, 'name': 'Test Company', 'postal_code': '12121', 'street': '16211',
                'total_rent': 337.5
            },
            {
                'city': '', 'id': self.company2.pk, 'name': 'Test Company2', 'postal_code': '', 'street': '', 'total_rent': 0
            }
        ]
        response = self.client.get('/api/companies/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.json())


class TestOfficeListViewSet(APITestCase, CompanyTestMixin):

    def setUp(self):
        self.setup_companies()

    def test_list_no_pk(self):
        data = []
        response = self.client.get('/api/company/offices/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.json())

    def test_list_with_pk1(self):
        data = [
            {
                'city': 'Cairo', 'id': self.headquarter.pk, 'monthly_rent': '12.50', 'postal_code': '12121',
                'street': '16211'
            },
            {
                'city': 'Cairo1', 'id': self.office1.pk, 'monthly_rent': '112.50', 'postal_code': '112121',
                'street': '162111'
            },
            {
                'city': 'Cairo2', 'id': self.office2.pk, 'monthly_rent': '212.50', 'postal_code': '121212',
                'street': '162112'
            }
        ]
        response = self.client.get('/api/company/offices/?pk={}'.format(self.company.pk))
        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.json())

    def test_list_with_pk2(self):
        data = []
        response = self.client.get('/api/company/offices/?pk={}'.format(self.company2.pk))
        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.json())


class TestChangeCompanyHeadQuarter(APITestCase, CompanyTestMixin):

    def setUp(self):
        self.setup_companies()

    def test_get_request(self):
        response = self.client.get(reverse('update_headquarter'))
        self.assertEqual(405, response.status_code)

    def test_no_request_data(self):
        errors = {'errors': {'company_id': ['This field is required.'], 'headquarter_id': ['This field is required.']}}
        response = self.client.post(reverse('update_headquarter'))
        self.assertEqual(400, response.status_code)
        self.assertEqual(errors, response.json())

    def test_invalid_type(self):
        errors = {'errors': {
            'company_id': ['A valid integer is required.'],
            'headquarter_id': ['A valid integer is required.']
        }}
        response = self.client.post(
            reverse('update_headquarter'),
            data={'company_id': 'test', 'headquarter_id': 'test'}
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(errors, response.json())

    def test_company_not_found(self):
        errors = {'errors': {'company_id': ['company not found']}}
        response = self.client.post(
            reverse('update_headquarter'),
            data={'company_id': 5000, 'headquarter_id': self.office1.pk}
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(errors, response.json())

    def test_office_not_found(self):
        errors = {'errors': {'headquarter_id': ['office not found']}}
        response = self.client.post(
            reverse('update_headquarter'),
            data={'company_id': self.company.pk, 'headquarter_id': 5000}
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(errors, response.json())

    def test_valid(self):
        self.assertEqual(self.headquarter.id, self.company.headquarter_id)
        response = self.client.post(
            reverse('update_headquarter'),
            data={'company_id': self.company.pk, 'headquarter_id': self.office1.pk}
        )
        self.assertEqual(200, response.status_code)
        self.company.refresh_from_db()
        self.assertEqual(self.office1.id, self.company.headquarter_id)
        self.assertEqual({'message': 'OK'}, response.json())