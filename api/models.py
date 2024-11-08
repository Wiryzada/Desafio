from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=120, unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.email})"


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_preparacao', 'Em preparação'),
        ('a_caminho', 'A caminho'),
        ('entregue', 'Entregue')
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    data_pedido = models.DateField()

    def __str__(self):
        return f"Pedido {self.id} - {self.status} - Total: R${self.total}"


class ItensPedido(models.Model):
    CATEGORIA_CHOICES = [
        ('bebida', 'Bebida'),
        ('sobremesa', 'Sobremesa'),
        ('salada', 'Salada'),
        ('acompanhamento', 'Acompanhamento')
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    nome = models.CharField(max_length=90)
    descricao = models.CharField(max_length=130)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return f"{self.nome} - R${self.preco} ({self.categoria})"

