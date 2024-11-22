from django.contrib import admin
from blog.models import Para

class Display_para_admin(admin.ModelAdmin):
    list_display_para = ('title_test','info_test')
# Register your models here.

admin.site.register(Para,Display_para_admin)
