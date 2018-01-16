from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$' , views.index , name='index'),
	url(r'^(?P<user_id>[0-9]+)/$' , views.detail , name='detail') 
]
	
