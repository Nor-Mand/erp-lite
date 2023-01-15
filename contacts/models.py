from django.db import models


# Persons
class Persons(models.Model):
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)

    class Meta:
        abstract = True


# Customers
class Customers(models.Model):
    pass


# Suppliers
class Suppliers(models.Model):
    pass


# Employees
class Employees(models.Model):
    pass


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