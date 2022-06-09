from django.shortcuts import render
from django.views.generic import ListView

from shop.models import *


def home(request):
    return render(request, 'content/main_p.html')


class Home(ListView):
    template_name = 'content/main_p.html'
    context_object_name = 'object'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        ctx['seo'] = Seo.objects.filter(url='main_p')[0]
        ctx['newTrue'] = Products.objects.filter(newTrue=True)[:5]
        ctx['recommendation'] = Products.objects.filter(recommendation=True)[:5]
        ctx['categorys'] = Category.objects.all()

        return ctx


class About(ListView):
    template_name = 'content/about.html'
    context_object_name = 'object'
    model = Seo

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(About, self).get_context_data(**kwargs)
        ctx['seo'] = Seo.objects.filter(url='about')[0]
        ctx['categorys'] = Category.objects.all()
        return ctx


class Contacts(ListView):
    template_name = 'content/contacts.html'
    context_object_name = 'object'
    model = Seo

    def get_context_data(self, *, object_list=None, **kwargs):
        self.slug = (self.request.path).split('/')[-1]
        ctx = super(Contacts, self).get_context_data(**kwargs)
        if Seo.objects.filter(url='contacts'):
            ctx['seo'] = Seo.objects.filter(url='contacts')[0]
        ctx['categorys'] = Category.objects.all()
        return ctx
