from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class CoreSitemap(Sitemap):
    priority = 0.8
    changefreq = 'yearly'
    protocol = 'https'

    def items(self):
        return ['core:home', 'core:about', 'core:contact', 'core:resume']  # , 'core:portfolio'

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, item):
        return '/blog/%s' % (item.slug)
