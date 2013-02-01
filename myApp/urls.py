from django.conf.urls import url,patterns
from myApp import views

urlpatterns = patterns('',

url(r'^$',views.index,name='index'),

url(r'^(?P<rec_id>\d+)/$',views.detail,name='detail'),
url(r'^add/$',views.add,name='add')


)
