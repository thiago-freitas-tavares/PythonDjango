from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


# 8. este módulo (models.py) já vem com o import models na criação do app products.

# 9. a classe Product herda todas as funções da classe Model do módulo models,
#    responsável por definir todas as características e comportamentos comuns dos
#    modelos numa aplicação Django.
