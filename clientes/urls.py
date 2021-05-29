from django.urls import path

from .views import lista_pessoa, nova_pessoa, atualiza_pessoa, deleta_pessoa

urlpatterns = [
    path('listar/', lista_pessoa, name='lista_pessoas'),
    path('novo/', nova_pessoa, name='nova_pessoa'),
    path('atualiza/<int:id>/', atualiza_pessoa, name='atualiza_pessoa'),
    path('detela/<int:id>/', deleta_pessoa, name='deleta_pessoas'),
]