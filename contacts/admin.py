from django.contrib import admin
from .models import Cities, Countries, Industries, Customers, Employees, Suppliers


admin.site.register(Cities)
admin.site.register(Countries)
admin.site.register(Industries)
admin.site.register(Customers)
admin.site.register(Employees)
admin.site.register(Suppliers)

class EmployeesAdmin(admin.ModelAdmin):
    model = Employees
    fields = ('first_name', 'last_name')