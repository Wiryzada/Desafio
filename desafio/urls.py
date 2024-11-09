# desafio/urls.py
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from api.views import usuario_router, pedido_router, itens_pedido_router

api = NinjaAPI()

api.add_router("/usuarios/", usuario_router)
api.add_router("/pedidos/", pedido_router)
api.add_router("/itens-pedido/", itens_pedido_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
