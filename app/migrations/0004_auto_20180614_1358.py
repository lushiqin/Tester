# Generated by Django 2.0.3 on 2018-06-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180614_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfromid',
            name='userId',
        ),
        migrations.AddField(
            model_name='userfromid',
            name='openId',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
