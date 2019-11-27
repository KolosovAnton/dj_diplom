from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from urllib.parse import urlencode
from django.views.generic import CreateView
from .models import Catalog, Categories, Product, Article, Review
from .forms import ReviewForm, LoginForm, RegisterForm


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(UserLoginView, self).form_valid(form)
        user = form.get_user()
        login(self.request, user)
        return valid


class UserRegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


def home_view(request):
    template = 'index.html'
    context = {}
    context['articles_list'] = Article.objects.order_by('-published_at')
    context['catalog_list'] = Catalog.objects.order_by('number')
    context['categories_list'] = Categories.objects.order_by('title').prefetch_related('catalog')
    context['products_list'] = Product.objects.order_by('name').prefetch_related('categories')
    context['name'] = 'home'
    return render(request, template, context)


def user_logout(request):
    logout(request)
    home_view(request)
    return HttpResponseRedirect('/')


def show_page(request, short_name):
    context = {}
    context['catalog_list'] = Catalog.objects.order_by('number')
    context['categories_list'] = Categories.objects.order_by('title').prefetch_related('catalog')
    context['products_list'] = Product.objects.order_by('name').prefetch_related('categories')

    for item in context['catalog_list']:
        if short_name == item.short_name:
            context['item'] = item
            context['name'] = item.title
            if not item.categories_set.all():
                if item.product_set.all():
                    template = 'shop/catalog.html'
                    context['product_list'] = item.product_set.all()
                else:
                    template = 'shop/empty_section.html'

    for item in context['categories_list']:
        if short_name == item.short_name:
            context['name'] = item.catalog.title
            if item.product_set.all():
                template = 'shop/categories.html'
                context['item'] = item
                count = 3
                page_num = int(request.GET.get('page', 1))
                paginator = Paginator(item.product_set.all(), count)
                page = paginator.get_page(page_num)
                data = page.object_list
                prev_page = urlencode({'page': page_num - 1})
                if page.has_previous():
                    prev_page_url = reverse('short_name', args=[item.short_name]) + f'?{prev_page}'
                else:
                    prev_page_url = None
                next_page = urlencode({'page': page_num + 1})
                if page.has_next():
                    next_page_url = reverse('short_name', args=[item.short_name]) + f'?{next_page}'
                else:
                    next_page_url = None
                context['products'] = data
                context['current_page'] = page_num
                context['prev_page_url'] = prev_page_url
                context['next_page_url'] = next_page_url
            else:
                template = 'shop/empty_section.html'

    for item in context['products_list']:
        if short_name == item.short_name:
            if item.catalog:
                context['name'] = item.catalog.title
            else:
                context['name'] = item.categories.catalog.title
            template = 'shop/phone.html'
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
