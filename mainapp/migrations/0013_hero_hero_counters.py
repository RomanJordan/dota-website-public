# Generated by Django 2.2.3 on 2019-08-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_hero_hero_attribute_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_counters',
            field=models.ManyToManyField(blank=True, related_name='_hero_hero_counters_+', to='mainapp.Hero'),
        ),
    ]
