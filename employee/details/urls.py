from django.conf.urls import include,url
from details import views
urlpatterns = [

    url(r'^income1/$', views.income1, name = 'income1'),
    url(r'^stored/$', views.stored, name = 'stored'),
    #url(r'^stored1/$', views.stored1, name = 'stored1'),

]
