from oscar.apps.catalogue.views import CatalogueView as CustomCatalogueView
from django.views.generic import TemplateView

class AboutUsView(TemplateView):
    template_name="oscar/catalogue/about-us.html"

# class CatalogueView(CustomCatalogueView):
#     context_object_name = "boutique"
#     template_name = "oscar/catalogue/custom-browse.html"


