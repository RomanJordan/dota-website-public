# Generated by Django 2.1.5 on 2019-07-25 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190722_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='hero_thumbnail',
            field=models.ImageField(default='Juggernaut_icon.png', upload_to='hero_thumbnails'),
        ),
    ]
