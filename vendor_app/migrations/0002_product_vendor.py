# Generated by Django 3.2.7 on 2021-09-24 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vendor_app.vendor'),
        ),
    ]
