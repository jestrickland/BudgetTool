from django.conf.urls import url
from . import views

#urlpatterns = [
    #url(r'^$', views.index)
#]

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'current', views.current, name='current'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^post_url/$', views.post_budgetitem, name='post_budgetitem')
]