# Generated by Django 2.2.3 on 2019-08-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_hero_hero_counters'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_advantages',
            field=models.ManyToManyField(blank=True, related_name='advantages', to='mainapp.Hero'),
        ),
    ]