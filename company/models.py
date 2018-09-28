from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField('Name', max_length=300)
    headquarter = models.OneToOneField('Office', on_delete=models.CASCADE, blank=True, null=True, related_name='head')

    @property
    def total_rent(self):
        result = 0
        for office in self.offices.all():
            if office.monthly_rent:
                result += office.monthly_rent
        return result

    @property
    def street(self):
        if self.headquarter:
            return self.headquarter.street or ""
        return ""

    @property
    def postal_code(self):
        if self.headquarter:
            return self.headquarter.postal_code or ""
        return ""

    @property
    def city(self):
        if self.headquarter:
            return self.headquarter.city or ""
        return ""


class Office(models.Model):
    company = models.ForeignKey(Company, related_name='offices', on_delete=models.CASCADE)
    street = models.CharField('Street', max_length=256, blank=True)
    postal_code = models.CharField('Postal Code', max_length=32, blank=True)
    city = models.CharField('City', max_length=128, blank=True, null=True)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
