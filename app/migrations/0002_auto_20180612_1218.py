# Generated by Django 2.0.3 on 2018-06-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfaceinfo',
            name='data',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='interfaceinfo',
            name='methodType',
            field=models.CharField(max_length=32, null=True),
        ),
    ]