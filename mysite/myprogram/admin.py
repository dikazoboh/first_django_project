from django.contrib import admin
from .models import Student, School,Grade, Faculty, Department, CertificateType

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(CertificateType)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Grade)