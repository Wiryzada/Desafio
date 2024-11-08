# Generated by Django 5.1.3 on 2024-11-08 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em_preparacao', 'Em preparação'), ('a_caminho', 'A caminho'), ('entregue', 'Entregue')], max_length=15)),
                ('data_pedido', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=120, unique=True)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('descricao', models.CharField(max_length=130)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('categoria', models.CharField(choices=[('bebida', 'Bebida'), ('sobremesa', 'Sobremesa'), ('salada', 'Salada'), ('acompanhamento', 'Acompanhamento')], max_length=20)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='api.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='api.usuario'),
        ),
    ]
