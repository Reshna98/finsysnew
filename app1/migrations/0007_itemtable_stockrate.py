# Generated by Django 4.2.2 on 2023-09-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_recurring_bill_recurringbill_item_repeatevery'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='stockrate',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
    ]