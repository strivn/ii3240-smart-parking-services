# Generated by Django 2.0.7 on 2019-05-15 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0025_auto_20190515_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingLot.Lot'),
        ),
    ]