# Generated by Django 2.0.7 on 2019-04-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_auto_20190424_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]