from django.db import models


# Global Information(Abstraction field)
class GlobalInformation(models.Model):
    GENDER = [
        ('', '----'),
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    first_name = models.CharField(max_length=220, default='')
    last_name = models.CharField(max_length=220, default='')
    email = models.EmailField(max_length=220, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    mobil_number = models.CharField(max_length=20, blank=True, default='')
    address = models.CharField(max_length=250, blank=True, default='')
    postcode = models.CharField(max_length=50, blank=True, default='')
    company_name = models.CharField(max_length=220, default='')
    job_title = models.CharField(max_length=20, blank=True, default='')
    gender = models.CharField(max_length=20, choices=GENDER, default='')

    class Meta:
        abstract = True


# Customers
class Customers(GlobalInformation):
    tax_id = models.CharField(max_length=20, blank=True, default='')


# Suppliers
class Suppliers(GlobalInformation):
    website = models.URLField(max_length=220, blank=True, default='')


# Employees
class Employees(GlobalInformation):
    birthday = models.DateField(blank=True, null=True, default='')


# Industries
class Industries(models.Model):
    name = models.CharField(max_length=220)
    description = models.CharField(max_length=220)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.description = self.description.upper()
        return super(Industries,self).save(*args, **kwargs)


# Countries
class Countries(models.Model):
    name = models.CharField(max_length=220)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.code = self.code.upper()
        return super(Countries, self).save(*args, **kwargs)


# Cities
class Cities(models.Model):
    name = models.CharField(max_length=220)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        return super(Cities, self).save(*args, **kwargs)