from django.conf.urls import include,url
from django.contrib import admin
from message import views
admin.autodiscover()

urlpatterns = [
	url(r'^$' , views.home , name='home'),
	url(r'^signup/$' , views.UserFormView.as_view() , name='signup '),
    url(r'^admin/', admin.site.urls),
    url(r'^inbox/', include('message.urls')),
    url(r'^polls/', include('polls.urls')),
]
