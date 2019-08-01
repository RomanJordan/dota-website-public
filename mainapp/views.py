from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Hero
from django.template import RequestContext



class HeroPageView(ListView):
    model = Hero
    template_name = 'mainapp/hero_list.html'
    context_object_name = 'heroes'


class HeroDetailView(DetailView):
    model = Hero
    query_pk_and_slug = False
    template_name = 'mainapp/hero_detail_view.html'

    def get_counters(self, **kwargs):
        context = super(HeroDetailView, self).get_context_data(**kwargs)
        context['counters'] = hero.hero_counters.objects.all()
        return context
