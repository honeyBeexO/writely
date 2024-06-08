from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('', views.home, name="quizz-home"),
    path('quizz/<int:waffel_id>/', views.waffles_quizz, name="waffles-quizz"),
    
]