from pyexpat import model
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Shelf)
admin.site.register(models.Book)
admin.site.register(models.Member)
admin.site.register(models.Loan)
