from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularSwaggerView
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("home.api.v1.urls")),
]

admin.site.site_header = "Cricket Scraper"
admin.site.site_title = "Cricket Scraper Admin Portal"
admin.site.index_title = "Cricket Scraper Admin"

# swagger
urlpatterns += [
    path("api-docs/schema/", SpectacularJSONAPIView.as_view(), name="schema"),
    path(
        "api-docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="api_docs"
    ),
]

urlpatterns += [re_path(r".*", TemplateView.as_view(template_name="index.html"))]
