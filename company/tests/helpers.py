from company.models import Company, Office


class CompanyTestMixin(object):
    def setup_companies(self):
        self.company = self.create_full_company()
        self.company2 = self.create_empty_company()

    def create_empty_company(self):
        return Company.objects.create(name='Test Company2')

    def create_full_company(self):
        company = Company.objects.create(name='Test Company')
        self.headquarter = Office.objects.create(
            company=company,
            street='16211',
            postal_code='12121',
            city='Cairo',
            monthly_rent=12.5,
        )
        self.office1 = Office.objects.create(
            company=company,
            street='162111',
            postal_code='112121',
            city='Cairo1',
            monthly_rent=112.5,
        )
        self.office2 = Office.objects.create(
            company=company,
            street='162112',
            postal_code='121212',
            city='Cairo2',
            monthly_rent=212.5,
        )
        company.headquarter = self.headquarter
        company.save()
        return company
