from django.urls import path # type: ignore
from . import views
app_name = 'quizz'
urlpatterns = [
    path('', views.index, name="index"),
    path('quizz/<int:waffel_id>/', views.waffles_quizz, name="waffles-quizz"),
    
]