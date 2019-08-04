from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
import itertools
from multiselectfield import MultiSelectField


class Item(models.Model):
    item_name = models.CharField(default='default', max_length=50, blank=False)
    item_stat1 = models.CharField(default='default', max_length=50, blank=True)
    item_stat2 = models.CharField(default='default', max_length=50, blank=True)
    item_stat3 = models.CharField(default='default', max_length=50, blank=True)
    item_stat4 = models.CharField(default='default', max_length=50, blank=True)
    item_stat5 = models.CharField(default='default', max_length=50, blank=True)
    item_stat6 = models.CharField(default='default', max_length=50, blank=True)
    item_stat7 = models.CharField(default='default', max_length=50, blank=True)
    item_stat8 = models.CharField(default='default', max_length=50, blank=True)
    item_stat9 = models.CharField(default='default', max_length=50, blank=True)
    item_stat10 = models.CharField(default='default', max_length=50, blank=True)
    item_description = models.CharField(default='default', max_length=50, blank=False)
    item_cost = models.IntegerField(default = 0, blank=False)
    item_image = models.ImageField(default='Juggernaut_icon.png', upload_to='item_thumbnails')




    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['item_name']


class Hero(models.Model):
    STRENGTH = 'STR'
    INTELLIGENCE = 'INT'
    AGILITY = 'AGI'


    ATTRIBUTES = [
        ('STRENGTH', 'Strength'),
        ('AGILITY', 'Agility'),
        ('INTELLIGENCE', 'Intelligence'),
    ]

    HERO_ROLES = (('RANGED', 'Ranged'),
              ('MELEE', 'Melee'),
              ('CARRY', 'Carry'),
              ('SUPPORT', 'Support'),
              ('NUKER', 'Nuker'),
              ('DISABLER', 'Disabler'),
              ('JUNGLER', 'Jungler'),
              ('DURABLE', 'Durable'),
              ('ESCAPE', 'Escape'),
              ('PUSHER', 'Pusher'),
              ('INITIATOR', 'Initiator'),
              ('ROAMER', 'Roamer'),)

    hero_name = models.CharField(max_length=50, default='Hero')
    hero_thumbnail = models.ImageField(default='Juggernaut_icon.png', upload_to='hero_thumbnails')
    hero_lore = models.TextField(default='Default hero lore')
    hero_main_attribute = models.CharField(choices=ATTRIBUTES, default=STRENGTH, max_length=12)
    hero_attribute_image = models.ImageField(default='Strength_attribute_symbol.png', upload_to='hero_thumbnails')
    hero_base_health = models.IntegerField(default=1000)
    hero_base_mana = models.IntegerField(default=25)
    hero_base_magic_res = models.IntegerField(default=25)
    hero_base_mana = models.IntegerField(default=25)
    hero_base_spell_dmg = models.IntegerField(default=25)
    hero_base_armor = models.IntegerField(default=25)
    hero_base_att_persec = models.IntegerField(default=25)
    hero_base_damage = models.IntegerField(default=25)
    hero_base_movement_speed = models.IntegerField(default=25)
    hero_roles = MultiSelectField(max_choices=6, choices=HERO_ROLES, blank=True)
    hero_counters = models.ManyToManyField("self", blank=True, symmetrical=False)
    hero_advantages = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='advantages')
    hero_recommended_items = models.ManyToManyField(Item, blank=True, symmetrical=False)

    hero_talent_left_lvl10 = models.CharField(default='default talent description', max_length=100)
    hero_talent_right_lvl10 = models.CharField(default='default talent description', max_length=100)
    
    hero_talent_left_lvl15 = models.CharField(default='default talent description', max_length=100)
    hero_talent_right_lvl15 = models.CharField(default='default talent description', max_length=100)
    
    hero_talent_left_lvl20 = models.CharField(default='default talent description', max_length=100)
    hero_talent_right_lvl20 = models.CharField(default='default talent description', max_length=100)
    
    hero_talent_left_lvl25 = models.CharField(default='default talent description', max_length=100)
    hero_talent_right_lvl25 = models.CharField(default='default talent description', max_length=100)
    
    
    slug = models.SlugField(max_length=30, null=True, blank=True)
    

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('HeroDetailView', kwargs=kwargs)


    def save(self, *args, **kwargs):
        max_length = self._meta.get_field('slug').max_length
        value = self.hero_name
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Hero.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.hero_name


    class Meta:
        ordering = ['hero_name']



