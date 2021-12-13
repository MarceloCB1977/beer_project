from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'beer'

urlpatterns = [
    # path('', HomePageView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('beer_list', views.beer_list, name='beer_list'),
    path('beer_form', views.beer_form, name='beer_form'),
    path('beer_search', views.beer_search, name='beer_search'),
    path('style_search', views.style_search, name='style_search'),
    path('beer_detail/<beer_id>', views.beer_detail, name='beer_detail'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
