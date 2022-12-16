from django.contrib import admin
from .models import Districts,Branch,Form
# Register your models here.
class AdminDistrict(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Districts,AdminDistrict)

class AdminBranch(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Branch,AdminBranch)



class AdminForm(admin.ModelAdmin):
    list_display = ['name','age','mailid','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Form,AdminForm)