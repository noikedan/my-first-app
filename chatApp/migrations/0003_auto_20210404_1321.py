# Generated by Django 2.2.19 on 2021-04-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0002_auto_20210404_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='year',
        ),
        migrations.AlterField(
            model_name='post',
            name='money',
            field=models.BigIntegerField(default=1000000),
        ),
    ]