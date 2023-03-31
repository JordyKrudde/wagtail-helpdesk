# Generated by Django 3.2.18 on 2023-03-31 13:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0001_initial'),
        ('experts', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertanswerrelationship',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_answer_relationship', to='experts.expert'),
        ),
        migrations.AddField(
            model_name='categoryanswerrelationship',
            name='answer',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_category_relationship', to='cms.answer'),
        ),
        migrations.AddField(
            model_name='categoryanswerrelationship',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_answer_relationship', to='cms.answercategory'),
        ),
        migrations.AddField(
            model_name='answertag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='cms.answer'),
        ),
        migrations.AddField(
            model_name='answertag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cms_answertag_items', to='taggit.tag'),
        ),
        migrations.AddField(
            model_name='answer',
            name='social_image',
            field=models.ForeignKey(blank=True, help_text='This is the image that will be displayed when sharing on social media', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='answer',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='cms.AnswerTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
