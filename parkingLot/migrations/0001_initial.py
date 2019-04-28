# Generated by Django 2.0.7 on 2019-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lot',
            fields=[
                ('lotID', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False, unique=True)),
                ('updateTime', models.DateTimeField(null=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]