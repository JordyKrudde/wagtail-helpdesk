# Generated by Django 3.2.16 on 2022-12-13 15:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_helpdesk.cms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0036_auto_20221213_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_origin',
            field=wagtail.fields.StreamField([('origin', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255)), ('content', wagtail.blocks.RichTextBlock(features=('bold', 'italic', 'link', 'document-link'), help_text="Clarification of the answer's origin")), ('sources', wagtail.blocks.ListBlock(wagtail_helpdesk.cms.blocks.ScientificSourceBlock))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='page_content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=('h2', 'h3', 'h4', 'image', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed', 'superscript', 'subscript')))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The recommended aspect ratio is landscape with a size of of 1920x1080. Portrait images not recommended.')), ('caption', wagtail.blocks.CharBlock(max_length=2500))])), ('quote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(max_length=1000))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='related_items',
            field=wagtail.fields.StreamField([('related_items', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(page_type=['cms.Answer'])))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='footersettings',
            name='about_buttons',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons'),
        ),
        migrations.AlterField(
            model_name='footersettings',
            name='expert_buttons',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons'),
        ),
        migrations.AlterField(
            model_name='footersettings',
            name='nav',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Navigation'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='header_buttons',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='recent_question_buttons',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons'),
        ),
        migrations.AlterField(
            model_name='mainnavsettings',
            name='buttons',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Title')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Page'))]))], blank=True, use_json_field=True, verbose_name='Buttons'),
        ),
        migrations.AlterField(
            model_name='stickysettings',
            name='buttons',
            field=wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons'),
        ),
    ]
