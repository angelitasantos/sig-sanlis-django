from django.contrib import admin
from .models import Partner, Category, UnMed, Item


admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(UnMed)
admin.site.register(Item)