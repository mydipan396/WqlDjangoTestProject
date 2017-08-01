
from django.conf.urls import url
from django.contrib import admin
from csdb import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.Home.as_view()),
    url(r'^detail-(\d+)-(\d+).html', views.detail),
    url(r'^orm', views.orm),
]