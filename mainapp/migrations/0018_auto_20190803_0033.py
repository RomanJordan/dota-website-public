# Generated by Django 2.2.3 on 2019-08-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_hero_hero_advantages'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_talent_left_lvl10',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_left_lvl15',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_left_lvl20',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_left_lvl25',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_right_lvl10',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_right_lvl15',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_right_lvl20',
            field=models.CharField(default='default talent description', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_talent_right_lvl25',
            field=models.CharField(default='default talent description', max_length=100),
        ),
    ]
