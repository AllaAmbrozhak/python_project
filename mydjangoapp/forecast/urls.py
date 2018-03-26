from django.urls import path
from forecast import views

urlpatterns = [
    path(r'', views.YourGeolocationView.as_view()),
    path(r'weather/', views.YourForecastView.as_view()),
]
