# Generated by Django 4.2.2 on 2023-09-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_rename_stockrate_itemtable_stock_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtable',
            name='stock_rate',
        ),
        migrations.AddField(
            model_name='itemtable',
            name='stockrate',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
    ]
