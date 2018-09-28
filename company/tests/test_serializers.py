from django.test import TestCase
from company.serializers import ChangeHeadQuarterSerializer
from rest_framework.exceptions import ValidationError

from company.tests.helpers import CompanyTestMixin


class TestChangeHeadQuarterSerializer(TestCase, CompanyTestMixin):

    def setUp(self):
        self.setup_companies()
        self.serializer = ChangeHeadQuarterSerializer()

    def test_validate_company_not_found(self):
        with self.assertRaises(ValidationError) as context:
            self.serializer.validate({"company_id": 5000})

        self.assertIn('company not found', str(context.exception))

    def test_validate_office_not_found(self):
        with self.assertRaises(ValidationError) as context:
            self.serializer.validate({"company_id": self.company.pk, 'headquarter_id': 5000})

        self.assertIn('office not found', str(context.exception))

    def test_valid(self):
        data_in = {"company_id": self.company.pk, 'headquarter_id': self.office1.pk}
        self.assertEqual(data_in, self.serializer.validate(data_in))