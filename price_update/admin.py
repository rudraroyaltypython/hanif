from django.contrib import admin
from price_update.models import MacPrice
from price_update.models import KingPrice
from price_update.models import PrawnsPrice


class MacPriceAdmin(admin.ModelAdmin):
    list_display = ['wholesale']

class KingPriceAdmin(admin.ModelAdmin):
    list_display = ['wholesale']

class PrawnsPriceAdmin(admin.ModelAdmin):
    list_display = ['wholesale']

# Register your models here.
admin.site.register(MacPrice,MacPriceAdmin)
admin.site.register(KingPrice,KingPriceAdmin)
admin.site.register(PrawnsPrice,PrawnsPriceAdmin)