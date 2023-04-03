# Generated by Django 3.2.18 on 2023-03-31 13:47

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('bio', models.TextField(verbose_name='biography')),
                ('affiliation', models.CharField(max_length=128, verbose_name='Affiliation')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
                ('twitter_profile', models.URLField(blank=True, null=True, verbose_name='Twitter Profile')),
                ('linkedin_profile', models.URLField(blank=True, null=True, verbose_name='LinkedIn Profile')),
                ('orcid_profile', models.URLField(blank=True, null=True, verbose_name='OrcID Link')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('areas_expertise', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='areas of expertise')),
                ('picture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
