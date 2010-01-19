from django.contrib import admin
from models import Company

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ( 'title', 'description', ) 
    filter_fields = ('is_active',)
    list_display = ( 'id', 'title', 'creation_date', 'modification_date', 'is_active')
    
admin.site.register(Company, CompanyAdmin)
