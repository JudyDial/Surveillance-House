# Generated by Django 4.2.4 on 2024-02-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(blank=True, choices=[('wire-free', 'Wire-Free'), ('indoor', 'Indoor'), ('outdoor', 'Outdoor')], max_length=100, null=True),
        ),
    ]
