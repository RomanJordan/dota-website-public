# Generated by Django 2.1.5 on 2019-07-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_herouniqueslug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herouniqueslug',
            name='hero_ptr',
        ),
        migrations.AddField(
            model_name='hero',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.DeleteModel(
            name='HeroUniqueSlug',
        ),
    ]
