from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]

# 4. import path e views - da própria pasta products - para referenciar as URLs
#    com suas respectivas funções view. path('URL inteira', função view).

# 5. primeiro argumento com uma string vazia representa a raiz (root) do app.

# 6. segundo argumento apenas referencia a função view, quem chama a função é o
#    Django qdo o navegador envia o HttpRequest para o servidor.
