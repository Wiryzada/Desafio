from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Usuario, Pedido, ItensPedido
from .schemas import (
    UsuarioSchema, UsuarioCreateSchema,
    PedidoSchema, PedidoCreateSchema,
    ItensPedidoSchema, ItensPedidoCreateSchema
)

# Router para Usuario
usuario_router = Router()

@usuario_router.get("/{usuario_id}", response=UsuarioSchema)
def get_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return usuario

@usuario_router.post("/", response=UsuarioSchema)
def create_usuario(request, data: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**data.dict())
    return usuario

@usuario_router.put("/{usuario_id}", response=UsuarioSchema)
def update_usuario(request, usuario_id: int, data: UsuarioCreateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in data.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return usuario

@usuario_router.delete("/{usuario_id}")
def delete_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}

# Router para Pedido
pedido_router = Router()

@pedido_router.get("/{pedido_id}", response=PedidoSchema)
def get_pedido(request, pedido_id: int):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return pedido

@pedido_router.post("/", response=PedidoSchema)
def create_pedido(request, data: PedidoCreateSchema):
    pedido = Pedido.objects.create(**data.dict())
    return pedido

@pedido_router.put("/{pedido_id}", response=PedidoSchema)
def update_pedido(request, pedido_id: int, data: PedidoCreateSchema):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    for attr, value in data.dict().items():
        setattr(pedido, attr, value)
    pedido.save()
    return pedido

@pedido_router.delete("/{pedido_id}")
def delete_pedido(request, pedido_id: int):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    return {"success": True}

# Router para ItensPedido
itens_pedido_router = Router()

@itens_pedido_router.get("/{item_id}", response=ItensPedidoSchema)
def get_itens_pedido(request, item_id: int):
    item = get_object_or_404(ItensPedido, id=item_id)
    return item

@itens_pedido_router.post("/", response=ItensPedidoSchema)
def create_itens_pedido(request, data: ItensPedidoCreateSchema):
    item = ItensPedido.objects.create(**data.dict())
    return item

@itens_pedido_router.put("/{item_id}", response=ItensPedidoSchema)
def update_itens_pedido(request, item_id: int, data: ItensPedidoCreateSchema):
    item = get_object_or_404(ItensPedido, id=item_id)
    for attr, value in data.dict().items():
        setattr(item, attr, value)
    item.save()
    return item

@itens_pedido_router.delete("/{item_id}")
def delete_itens_pedido(request, item_id: int):
    item = get_object_or_404(ItensPedido, id=item_id)
    item.delete()
    return {"success": True}
