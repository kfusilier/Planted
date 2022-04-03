from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
	path('', views.Home.as_view(), name="home"),
	path('about/', views.About.as_view(), name='about'), 
	path('plants/', views.Plant_List.as_view(), name='plant_list'), 
	path('profile/', views.Profile.as_view(), name='profile'), 
	path('plant_detail/', views.Plant_Detail.as_view(), name='plant_detail'), 
	path('note_detail/', views.Note_Detail.as_view(), name='note_detail'), 
	path('calendar/', views.Calendar.as_view(), name='calendar'),
]

	# path('signup/', views.About.as_view(), name='signup'), 
	# path('login/', views.About.as_view(), name='login'), 
	# path('', views.About.as_view(), name='logout'),