from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.ListView.as_view(), name="lista"),
		url(r'^nuevo/$', views.FormView.as_view(),name="nuevo"),
]