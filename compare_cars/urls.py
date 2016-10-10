# urlpatterns = [
    
#     url(r'^$',views.Get_allMakes.as_view(), name='make_index'),
#     # url(r'^(?P<car_makes>[A-Za-z0-9\w @%._-]+)/make_models/$', views.make_models, name='make_models'),
    
# ]



from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('',
    url(r'^$', views.Get_allMakes.as_view(), name='make_list'),
    # url(r'^(?P<car_makes>[A-Za-z0-9\w @%._-]+)/make_models/$', views.make_models, name='model-list'),
)


urlpatterns = format_suffix_patterns(urlpatterns)

