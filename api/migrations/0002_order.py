# Generated by Django 5.0.2 on 2024-02-19 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
        ),
    ]