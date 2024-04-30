from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ScraperViewset


router = DefaultRouter()
router.register(r'scrapers', ScraperViewset, basename='scraper')

urlpatterns = [
    
]

urlpatterns += router.urls
