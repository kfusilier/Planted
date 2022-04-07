from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
	path('', views.Home.as_view(), name="home"),
	path('about/', views.About.as_view(), name='about'), 
	path('profile/', views.Profile.as_view(), name='profile'),  
	path('calendar/', views.Calendar.as_view(), name='calendar'),

	path('plants/', views.Plant_List.as_view(), name='plant_list'),
	path('plants/new/', views.Plant_Create.as_view(), name='plant_create'),
	path('plants/<int:pk>/', views.Plant_Detail.as_view(), name='plant_detail'),
	path('plants/<int:pk>/update', views.Plant_Update.as_view(), name='plant_update'),
	path('plants/<int:pk>/delete', views.Plant_Delete.as_view(), name='plant_delete'),

	path('notes/', views.Note_List.as_view(), name='note_list'), 	
	path('notes/new/', views.Note_Create.as_view(), name='note_create'),
	path('notes/<int:pk>/', views.Note_Detail.as_view(), name='note_detail'),
	path('notes/<int:pk>/update', views.Note_Update.as_view(), name='note_update'),
	path('notes/<int:pk>/delete', views.Note_Delete.as_view(), name='note_delete'),

	# path('pests/', views.pests_index, name='pests_list'),
]

	# path('signup/', views.About.as_view(), name='signup'), 
	# path('login/', views.About.as_view(), name='login'), 
	# path('', views.About.as_view(), name='logout'),