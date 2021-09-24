# Generated by Django 3.2.7 on 2021-09-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14)),
                ('city', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
    ]
