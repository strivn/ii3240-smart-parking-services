# Generated by Django 2.1.7 on 2019-04-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0005_auto_20190424_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.CharField(max_length=30),
        ),
    ]
