from . import views
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'employer'

urlpatterns = [
	path('', views.dashboard, name='cdashboard'),
	path('newjob/', views.newjob, name='newjob'),
	path('edit_profile/', views.edit, name='cedit'),
	path('manage_job/', views.manage, name='manage'),
	path('candidates/', views.candidates, name='candidates'),
	path('subscriptions/', views.subscriptions, name='subscriptions'),
	path('change_pass/', views.change_pass, name='change_pass'),
	path('cinbox/', views.cinbox, name='cinbox'),
	path('cnotifications/', views.cnotifications, name='cnotifications'),
	path('under_development/', views.under_development, name='under_development'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)