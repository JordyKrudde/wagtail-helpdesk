# Generated by Django 3.1.13 on 2021-09-18 09:50

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('cms', '0026_auto_20201108_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(max_length=128)),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('outro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
