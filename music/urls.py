from django.urls import path, include
from music import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'concerts', views.ConcertViewSet, basename='concert')
router.register(r'songs', views.SongViewSet, basename='song')
router.register(r'parts', views.PartViewSet, basename='part')
router.register(r'files', views.FileViewSet, basename='file')
router.register(r'performances', views.PerformanceViewSet, basename='performance')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]