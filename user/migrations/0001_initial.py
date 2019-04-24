# Generated by Django 2.1.7 on 2019-04-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=50)),
                ('userEmail', models.CharField(max_length=50)),
                ('userPhone', models.CharField(max_length=13)),
                ('cardNumber', models.CharField(max_length=50)),
                ('userMoney', models.PositiveIntegerField()),
            ],
        ),
    ]