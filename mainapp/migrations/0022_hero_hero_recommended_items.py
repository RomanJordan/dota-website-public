# Generated by Django 2.2.3 on 2019-08-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20190804_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_recommended_items',
            field=models.ManyToManyField(blank=True, to='mainapp.Item'),
        ),
    ]
