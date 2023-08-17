from django.contrib import admin
from .models import Product, Offer



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)

# 11. classe ModelAdmin permite o gerenciamento de tabelas no 127.0.0.1.8000/admin.
#     atributo list_display é um tuple que especifica as colunas que serão visíveis
#     no 127.0.0.1.8000/admin.