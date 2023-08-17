from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
#   return HttpResponse('New Products:')
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products:')

# 1. este módulo (views.py) já vem com o import render na criação do app products.

# 2. todas as funções view devem receber um parâmetro, que é o http request passado
#    quando o usuário acessa a página.

# 3. por enquanto vamos apenas retornar uma mensagem para o navegador e para isso
#    precisamos impotar o método HttpResponse.

# 12. método objects.all recupera todos os dados da tabela em questão do DB, mas
#     temos também objects.filter, objects.get, objects.save, por exemplo.

# 13. render( objeto argumento da função index,
#             nome do template,
#             key-value pair {'palavra_chave': objeto com os dados recuperados} )
