# Generated by Django 2.0.3 on 2018-08-06 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180803_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercanvas',
            name='moblie',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
