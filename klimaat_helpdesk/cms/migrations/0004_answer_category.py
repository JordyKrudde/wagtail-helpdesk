# Generated by Django 2.2.9 on 2020-01-12 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20200111_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='cms.AnswerCategory'),
        ),
    ]
