from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
from django.contrib.auth import views as logViews

urlpatterns = [
	url(r'^registro/$', views.RegistrationView.as_view(),name="registro"),
	url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
	url(r'^search/$', views.UserListView.as_view(), name="search"),
	url(r'^detalle/(?P<id>[0-9]+)/$', views.UserDetailView.as_view(), name="detalle"),
	url(r'^login/$', logViews.login, name="login"),
	url(r'^logout/$', logout, name="logout")
]