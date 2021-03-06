# Generated by Django 2.2.3 on 2019-08-04 04:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_hero_hero_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='default', max_length=50)),
                ('item_description', models.CharField(default='default', max_length=50)),
                ('item_cost', models.IntegerField(default=0)),
                ('item_image', models.ImageField(default='Juggernaut_icon.png', upload_to='item_thumbnails')),
            ],
            options={
                'ordering': ['item_name'],
            },
        ),
        migrations.AlterField(
            model_name='hero',
            name='hero_roles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('RANGED', 'Ranged'), ('MELEE', 'Melee'), ('CARRY', 'Carry'), ('SUPPORT', 'Support'), ('NUKER', 'Nuker'), ('DISABLER', 'Disabler'), ('JUNGLER', 'Jungler'), ('DURABLE', 'Durable'), ('ESCAPE', 'Escape'), ('PUSHER', 'Pusher'), ('INITIATOR', 'Initiator'), ('ROAMER', 'Roamer')], max_length=88),
        ),
    ]
