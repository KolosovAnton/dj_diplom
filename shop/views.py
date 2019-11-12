from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from urllib.parse import urlencode
from .models import Catalog, Categories, Product, Article, Review
from .forms import ReviewForm


def home_view(request):
    template = 'index.html'
    context = {}
    article = Article.objects.order_by('-published_at')
    context['articles_list'] = article

    catalog = Catalog.objects.order_by('number')
    context['catalog_list'] = catalog

    categories = Categories.objects.order_by('title').prefetch_related('catalog')
    context['categories_list'] = categories

    product = Product.objects.order_by('name').prefetch_related('categories')
    context['products_list'] = product

    return render(request, template, context)


def show_page(request, short_name):
    context = {}
    context['catalog_list'] = Catalog.objects.order_by('number')
    context['categories_list'] = Categories.objects.order_by('title').prefetch_related('catalog')
    context['products_list'] = Product.objects.order_by('name').prefetch_related('categories')

    catalog = Catalog.objects.all()
    categories = Categories.objects.all()
    product = Product.objects.all()

    for item in catalog:
        if short_name == item.short_name:
            context['item'] = item
            categories_list = []
            catalog_list = []
            for categories_item in categories:
                catalog_list.append(categories_item.catalog)
                if categories_item.catalog == item:
                    categories_list.append(categories_item)
            # product_list = []
            # for product_item in product:
            #     product_list.append(product_item.catalog)
            if item in catalog_list:
                template = 'catalog.html'
                context['categories_list'] = categories_list
            else:
                template = 'empty_section.html'

    for item in categories:
        if short_name == item.short_name:
            categories_list = []
            for product_item in product:
                categories_list.append(product_item.categories)
            if item in categories_list:
                template = 'categories.html'
                context['item'] = item
                product_list = []
                for product_item in product:
                    if product_item.categories == item:
                        product_list.append(product_item)
                count = 3
                page_num = int(request.GET.get('page', 1))
                paginator = Paginator(product_list, count)
                page = paginator.get_page(page_num)
                data = page.object_list
                prev_page = urlencode({'page': page_num - 1})
                if page.has_previous():
                    prev_page_url = reverse('short_name', args=[item.short_name]) + '?{}'.format(prev_page)
                else:
                    prev_page_url = None
                next_page = urlencode({'page': page_num + 1})
                if page.has_next():
                    next_page_url = reverse('short_name', args=[item.short_name]) + '?{}'.format(next_page)
                else:
                    next_page_url = None
                context['products'] = data
                context['current_page'] = page_num
                context['prev_page_url'] = prev_page_url
                context['next_page_url'] = next_page_url
            else:
                template = 'empty_section.html'

    for item in product:
        if short_name == item.short_name:
            template = 'phone.html'
            context['item'] = item
            if request.method == 'POST':
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.product_id = item.id
                    review.save()
                    return HttpResponseRedirect(reverse('short_name', args=[item.short_name]))
            else:
                form = ReviewForm()
            context['reviews'] = Review.objects.filter(product=item)
            context['form'] = form

    return render(request, template, context)
