from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.views.decorators.cache import cache_page


# @cache_page(60 * 15)
# def shop_main(request):
#     return render(request, 'shop/main_shop.html')

class Shop_main(ListView):
    template_name = 'shop/main_shop.html'
    ordering = ['-id']
    context_object_name = 'object'

    def dispatch(self, request, *args, **kwargs):
        self.model = Category
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_main, self).get_context_data(**kwargs)
        # ctx = Product.objects.filter(vendorСode__icontains='1234')
        ctx['seo'] = Seo.objects.filter(url='shop')[0]
        ctx['products'] = Products.objects.all()
        ctx['categorys'] = Category.objects.all()

        return ctx


class Shop_category(ListView):
    paginate_by = 1
    template_name = 'shop/shop_category.html'
    ordering = ['-id']
    context_object_name = 'object'

    def dispatch(self, request, *args, **kwargs):

        self.slug = (self.request.path).split('/')[-1]
        self.model = Category
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):

        if self.model.objects.filter(slug=self.slug):
            title = self.model.objects.filter(slug=self.slug)[0].title
            ctx = super(Shop_category, self).get_context_data(**kwargs)
            # ctx = Product.objects.filter(vendorСode__icontains='1234')
            if Seo.objects.filter(url=self.slug):
                ctx['seo'] = Seo.objects.filter(url=self.slug)[0]
            ctx['products'] = Products.objects.all()
            ctx['categorys'] = Category.objects.all()
            ctx['slug'] = self.slug
            ctx['title'] = title
            return ctx
        else:
            self.template_name = '404.html'
            return


class Shop_detail_page(DetailView):
    template_name = 'shop/shop_detail.html'
    context_object_name = 'object'

    def dispatch(self, request, *args, **kwargs):
        self.slug_category = (self.request.path).split('/')[-2]
        self.slug_tovar = (self.request.path).split('/')[-1]
        self.model = Products
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):

        ctx = super(Shop_detail_page, self).get_context_data(**kwargs)
        request = self.request
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
        ctx['product'] = self.model.objects.filter(slug=self.slug_tovar)[0]
        return ctx

