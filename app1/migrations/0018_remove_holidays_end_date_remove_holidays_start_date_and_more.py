# Generated by Django 4.2.2 on 2023-10-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_itemtable_stock_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidays',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='holidays',
            name='start_date',
        ),
        migrations.AddField(
            model_name='holidays',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='stock_rate',
            field=models.FloatField(blank=True, default='0.0', null=True),
        ),
    ]