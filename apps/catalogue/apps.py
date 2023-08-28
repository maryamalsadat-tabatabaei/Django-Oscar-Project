import oscar.apps.catalogue.apps as apps
from django.urls import path, re_path
from oscar.core.loading import get_class
# from .views import AboutUsView

class CatalogueConfig(apps.CatalogueConfig):
    name = 'apps.catalogue'

    def ready(self):
        super().ready()
        self.about_us_view = get_class(
            'catalogue.views', 'AboutUsView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            re_path(r'^about-us/$',
                    self.about_us_view.as_view(), name='about-us'),
        ]
        return self.post_process_urls(urls)