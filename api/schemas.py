from ninja import Schema
from decimal import Decimal
from datetime import date

class UsuarioSchema(Schema):
    id: int
    nome: str
    email: str

class UsuarioCreateSchema(Schema):
    nome: str
    email: str
    senha: str

class PedidoSchema(Schema):
    id: int
    usuario_id: int
    total: Decimal
    status: str
    data_pedido: date

class PedidoCreateSchema(Schema):
    usuario_id: int
    total: Decimal
    status: str
    data_pedido: date

class ItensPedidoSchema(Schema):
    id: int
    pedido_id: int
    nome: str
    descricao: str
    preco: Decimal
    categoria: str

class ItensPedidoCreateSchema(Schema):
    pedido_id: int
    nome: str
    descricao: str
    preco: Decimal
    categoria: str
