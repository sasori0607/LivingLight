from django.shortcuts import render
from django.views.generic import ListView

from shop.models import *


def home(request):
    return render(request, 'content/main_p.html')


class About(ListView):

    template_name = 'content/about.html'
    context_object_name = 'object'
    model = Seo

    def get_context_data(self, *, object_list=None, **kwargs):
        self.slug = (self.request.path).split('/')[-1]
        ctx = super(About, self).get_context_data(**kwargs)
        if Seo.objects.filter(url=self.slug):
            ctx['seo'] = Seo.objects.filter(url=self.slug)[0]

        return ctx


class Contacts(ListView):

    template_name = 'content/contacts.html'
    context_object_name = 'object'
    model = Seo

    def get_context_data(self, *, object_list=None, **kwargs):
        self.slug = (self.request.path).split('/')[-1]
        ctx = super(Contacts, self).get_context_data(**kwargs)
        if Seo.objects.filter(url=self.slug):
            ctx['seo'] = Seo.objects.filter(url=self.slug)[0]

        return ctx