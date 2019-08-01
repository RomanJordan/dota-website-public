from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
import itertools

class Hero(models.Model):
    STRENGTH = 'STR'
    INTELLIGENCE = 'INT'
    AGILITY = 'AGI'


    ATTRIBUTES = [
        ('STRENGTH', 'Strength'),
        ('AGILITY', 'Agility'),
        ('INTELLIGENCE', 'Intelligence'),
    ]


    hero_name = models.CharField(max_length=50, default='Hero')
    hero_thumbnail = models.ImageField(default='Juggernaut_icon.png', upload_to='hero_thumbnails')
    hero_lore = models.TextField(default='Default hero lore')
    hero_main_attribute = models.CharField(choices=ATTRIBUTES, default=STRENGTH, max_length=12)
    hero_base_health = models.IntegerField(default=1000)
    hero_base_mana = models.IntegerField(default=25)
    hero_base_magic_res = models.IntegerField(default=25)
    hero_base_mana = models.IntegerField(default=25)
    hero_base_spell_dmg = models.IntegerField(default=25)
    hero_base_armor = models.IntegerField(default=25)
    hero_base_att_persec = models.IntegerField(default=25)
    hero_base_damage = models.IntegerField(default=25)
    hero_base_movement_speed = models.IntegerField(default=25)
    hero_attribute_image = models.ImageField(default='Strength_attribute_symbol.png', upload_to='hero_thumbnails')
    hero_counters = models.ManyToManyField("self", blank=True, symmetrical=False)
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
