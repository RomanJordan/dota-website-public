# Generated by Django 2.2.3 on 2019-08-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_hero_hero_recommended_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_stats',
            field=models.CharField(default='default', max_length=50),
        ),
    ]
