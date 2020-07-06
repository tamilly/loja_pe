# Generated by Django 3.0.7 on 2020-07-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20200706_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('BELEZA', 'Beleza'), ('LIMPEZA', 'Limpeza'), ('ALIMENTO', 'Alimento'), ('CASA', 'Casa'), ('OUTROS', 'Outros')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='validity',
            field=models.DateField(),
        ),
    ]