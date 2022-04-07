from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
	path('', views.Home.as_view(), name="home"),
	path('about/', views.About.as_view(), name='about'), 
	path('plants/', views.Plant_List.as_view(), name='plant_list'), 
	path('profile/', views.Profile.as_view(), name='profile'), 
	path('note_detail/', views.Note_Detail.as_view(), name='note_detail'), 
	path('calendar/', views.Calendar.as_view(), name='calendar'),
	path('plants/new/', views.Plant_Create.as_view(), name='plant_create'),
	path('plants/<int:pk>/', views.Plant_Detail.as_view(), name='plant_detail'),
	path('plants/<int:pk>/update', views.Plant_Update.as_view(), name='plant_update'),
]

	# path('signup/', views.About.as_view(), name='signup'), 
	# path('login/', views.About.as_view(), name='login'), 
	# path('', views.About.as_view(), name='logout'),