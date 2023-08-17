from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

# 10. módulo apps.py criado automaticamente com o app products, já incluindo
#     import AppConfig, class ProductsConfig e atributos default_auto_field/name.
