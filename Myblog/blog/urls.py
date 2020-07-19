from django.urls import path

from blog.views import list_blog


urlpatterns = [
    path('list/', list_blog)


]