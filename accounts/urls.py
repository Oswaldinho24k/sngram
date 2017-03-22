from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
from django.contrib.auth import views as logViews

urlpatterns = [
	url(r'^registro/$', views.RegistrationView.as_view(),name="registro"),
	url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
	url(r'^login/$', logViews.login, name="login"),
	url(r'^logout/$', logout, name="logout")
]