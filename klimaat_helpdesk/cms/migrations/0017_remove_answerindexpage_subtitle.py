# Generated by Django 3.0.5 on 2020-08-11 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20200810_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerindexpage',
            name='subtitle',
        ),
    ]
