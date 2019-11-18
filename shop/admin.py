from django.contrib import admin
from shop.models import Categories, Product, Catalog, Article, Review, Users


class UserInLine(admin.ModelAdmin):
    model = Users
    can_delete = False
    # list_display = ('title', 'number',)
    # list_filter = ('number', 'title',)
    # search_fields = ('number', 'title',)
    # ordering = ('number',)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'number',)
    list_filter = ('number', 'title',)
    search_fields = ('number', 'title',)
    ordering = ('number',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('title', 'published_at')
    search_fields = ('title', 'published_at')
    ordering = ('-published_at',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')


admin.site.register(Users, UserInLine)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Review, ReviewAdmin)
