# Generated by Django 2.1.5 on 2019-07-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_thumbnail',
            field=models.ImageField(default='hero_thumbnails/Juggernaut_icon.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='hero',
            name='hero_name',
            field=models.CharField(default='Hero', max_length=50),
        ),
    ]
