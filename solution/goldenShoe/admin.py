from django.contrib import admin
from .models import Product, Item , Cart 


#class to display AutoField product ID in PostAdmin
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['product_id']

    def display_id(self, obj):
        return obj.product_id

admin.site.register(Product, PostAdmin)
admin.site.register(Item)
admin.site.register(Cart)
