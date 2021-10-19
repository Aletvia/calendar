from django.urls import path
from .views import properties as prop
from .views import activities as act


urlpatterns = [
    path(
        'properties/<str:id>/',
        prop.PropertiesView.as_view(),
        name='properties'
    ),
    path(
        'activities/<str:start_date>/<str:end_date>/',
        act.ActivitiesView.as_view(),
        name='activities'
    ),
    path(
        'activities/<str:info>/',
        act.ActivitiesView.as_view(),
        name='activities'
    ),
    path(
        'activities/',
        act.ActivitiesView.as_view(),
        name='activities'
    ),
]