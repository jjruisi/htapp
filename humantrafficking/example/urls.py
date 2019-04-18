from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^ajax/test_ajax/$', views.test_ajax, name='test_ajax'),
]
