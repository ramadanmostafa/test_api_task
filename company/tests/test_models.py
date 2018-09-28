from django.test import TestCase

from company.tests.helpers import CompanyTestMixin


class TestCompanyModel(TestCase, CompanyTestMixin):
    def setUp(self):
        self.setup_companies()

    def test_total_rent(self):
        self.assertEqual(337.5, self.company.total_rent)
        self.assertEqual(0, self.company2.total_rent)

    def test_street(self):
        self.assertEqual('16211', self.company.street)
        self.assertEqual('', self.company2.street)

    def test_postal_code(self):
        self.assertEqual('12121', self.company.postal_code)
        self.assertEqual('', self.company2.postal_code)

    def test_city(self):
        self.assertEqual('Cairo', self.company.city)
        self.assertEqual('', self.company2.city)