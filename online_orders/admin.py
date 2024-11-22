from django.contrib import admin
from .models import Order
from .models import OrderPDF

class OrderAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('id', 'name', 'fish', 'quantity', 'total_price', 'order_date')

    # Fields to search
    search_fields = ('name', 'fish', 'place', 'contact')

    # Filters for the list view
    list_filter = ('fish', 'order_date')

    # Read-only fields (if you don't want total_price to be editable in the admin panel)
    readonly_fields = ('total_price',)

    # Fieldsets (optional): Group related fields together
    fieldsets = (
        ("Customer Information", {
            'fields': ('name', 'place', 'contact')
        }),
        ("Order Details", {
            'fields': ('fish', 'quantity', 'total_price')
        }),
        ("Date Information", {
            'fields': ('order_date',)
        }),
    )


class OrderPDFAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('id', 'order', 'pdf_file', 'generated_at')

    # Fields to search
    search_fields = ('order__name', 'order__fish')

    # Filters for the list view
    list_filter = ('generated_at',)

    # Read-only fields (if PDF is auto-generated)
    readonly_fields = ('pdf_file', 'generated_at')

class OrderPDFInline(admin.StackedInline):
    model = OrderPDF
    extra = 0
    readonly_fields = ('pdf_file', 'generated_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fish', 'quantity', 'total_price', 'order_date')
    search_fields = ('name', 'fish', 'place', 'contact')
    list_filter = ('fish', 'order_date')
    readonly_fields = ('total_price',)
    inlines = [OrderPDFInline]

# Register the model
admin.site.register(OrderPDF, OrderPDFAdmin)
# Register the model with the custom admin
admin.site.register(Order, OrderAdmin)
