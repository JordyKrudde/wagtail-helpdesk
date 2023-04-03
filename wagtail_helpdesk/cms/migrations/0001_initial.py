# Generated by Django 3.2.18 on 2023-03-31 13:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.fields
import wagtail.images.blocks
import wagtail_helpdesk.cms.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('type', models.CharField(choices=[('answer', 'Antwoord'), ('column', 'Column')], default='answer', help_text='Choose between answer or discussion piece with a more prominent look', max_length=100)),
                ('featured', models.BooleanField(default=False)),
                ('content', wagtail.fields.RichTextField(blank=True)),
                ('excerpt', models.CharField(help_text='This helps with search engines and when sharing on social media', max_length=255, null=True, verbose_name='Short description')),
                ('introduction', models.TextField(blank=True, default='', help_text='This text is displayed above the tags, useful as a TLDR section', null=True, verbose_name='Introduction')),
                ('page_content', wagtail.fields.StreamField([('richtext', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=('h2', 'h3', 'h4', 'image', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed', 'superscript', 'subscript')))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The recommended aspect ratio is landscape with a size of of 1920x1080. Portrait images not recommended.')), ('caption', wagtail.blocks.CharBlock(max_length=2500))])), ('quote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(max_length=1000))]))], use_json_field=True)),
                ('answer_origin', wagtail.fields.StreamField([('origin', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255)), ('content', wagtail.blocks.RichTextBlock(features=('bold', 'italic', 'link', 'document-link'), help_text="Clarification of the answer's origin")), ('sources', wagtail.blocks.ListBlock(wagtail_helpdesk.cms.blocks.ScientificSourceBlock))]))], blank=True, use_json_field=True)),
                ('related_items', wagtail.fields.StreamField([('related_items', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(page_type=['cms.Answer'])))]))], blank=True, use_json_field=True)),
            ],
            options={
                'ordering': ['-first_published_at'],
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AnswerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify the category', verbose_name='slug')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Answer Category',
                'verbose_name_plural': 'Answer Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AnswerIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='AnswerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AskQuestionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(default='<p>Wij willen je vraag graag zo compleet en correct mogelijk beantwoorden. Daarom vragen wij twee experts die voor jou aan de slag gaan om een antwoord te formuleren. De één doorzoekt bronnen en discussiëert, de ander gaat alles nog eens grondig controleren. Het kost wel wat tijd om deze wetenschappelijke standaard voor een betrouwbaar antwoord te behalen. Daarom kan het wat langer duren voordat je vraag beantwoord is.</p>', verbose_name='Intro')),
                ('step_1_title', models.CharField(default='Waar gaat je vraag over?', max_length=255, verbose_name='Titel')),
                ('step_2_title', models.CharField(default='Formuleer je vraag', max_length=255, verbose_name='Titel')),
                ('keep_me_posted_title', models.CharField(default='Bedankt voor je vraag!', max_length=255, verbose_name='Titel')),
                ('keep_me_posted_text', wagtail.fields.RichTextField(default='<p>Laat je mailadres achter als je op de hoogte gehouden wilt worden. Dit is optioneel.</p>', verbose_name='Tekst')),
                ('thank_you_text', wagtail.fields.RichTextField(default='<p>Bedankt voor het stellen van je vraag. We nemen je vraag in behandeling en proberen zo snel mogelijk een expert te vinden die je vraag kan beantwoorden.</p>', verbose_name='Tekst')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='CategoryAnswerRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExpertAnswerOverviewPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ExpertIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(max_length=128)),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('outro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GeneralPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(blank=True, max_length=128)),
                ('content', wagtail.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True)),
                ('header_buttons', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons')),
                ('recent_question_title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('recent_question_buttons', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons')),
            ],
            options={
                'verbose_name': 'Homepage',
                'verbose_name_plural': 'Homepages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='QuestionsInProgressPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Questions in progress page',
                'verbose_name_plural': 'Questions in progress pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SearchWidgetPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(default='Create a search widget to place on your own website')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='VolunteerIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(max_length=128)),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('outro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StickySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default="Didn't find the answer you were looking for? Check out the pending questions or ask your own question!", max_length=255, verbose_name='Text')),
                ('buttons', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Sticky menu',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_handle', models.CharField(blank=True, max_length=15, verbose_name='Twitter handle')),
                ('short_site_name', models.CharField(blank=True, max_length=255, verbose_name='Short site name')),
                ('short_site_description', models.CharField(blank=True, max_length=255, verbose_name='Short site description')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainNavSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default="Didn't find the answer you were looking for?", max_length=255, verbose_name='Text')),
                ('buttons', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Title')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Page'))]))], blank=True, use_json_field=True, verbose_name='Buttons')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Main navigation',
            },
        ),
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('about_text', wagtail.fields.RichTextField(blank=True, verbose_name='Text')),
                ('about_buttons', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons')),
                ('expert_title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('expert_text', wagtail.fields.RichTextField(blank=True, verbose_name='Text')),
                ('expert_buttons', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Buttons')),
                ('initiator_text', wagtail.fields.RichTextField(default='<p>An initiative of <a href="#">...</a> & <a href="#">...</a></p>', verbose_name='Initiator-text')),
                ('nav', wagtail.fields.StreamField([('item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='Titel')), ('page', wagtail.blocks.PageChooserBlock(verbose_name='Pagina'))]))], blank=True, use_json_field=True, verbose_name='Navigation')),
                ('maintainer_text', models.TextField(default='example.com is managed by ..., a non-profit organization, registered under Chamber of Commerce number ...', max_length=255, verbose_name='Maintainer text')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='ExpertAnswerRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('answer', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_expert_relationship', to='cms.answer')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
