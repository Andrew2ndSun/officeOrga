from django.conf.urls import include, url
import Home.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', Home.views.index, name='index'),
    url(r'^home$', Home.views.index, name='home'),
]