# Generated by Django 4.2.2 on 2023-10-03 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_itemtable_stock_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='holidays',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False, verbose_name='hid')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
