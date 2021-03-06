# Generated by Django 3.0.7 on 2020-07-06 21:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('cpf', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('birth_date', models.DateTimeField(blank=True)),
                ('password', models.CharField(max_length=20)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_code', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('category', models.CharField(max_length=50)),
                ('validity', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.User')),
            ],
        ),
    ]
