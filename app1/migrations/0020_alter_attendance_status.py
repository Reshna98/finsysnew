# Generated by Django 4.2.2 on 2023-10-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_rename_date_holidays_end_date_holidays_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(blank=True, default='Present', max_length=100, null=True),
        ),
    ]