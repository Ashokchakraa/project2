from django.contrib import admin
from MyProducts.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ("volume", )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["description"]
        else:
            return []
