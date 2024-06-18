from django.urls import path # type: ignore
from . import views
app_name = 'quizz'
urlpatterns = [
    path('', views.index, name="index"),
    path('waffels/',views.WaffelListView.as_view(),name='waffels'),
    path('crepes/',views.CrepesListView.as_view(),name='crepes'),
    path('cookies/',views.CookieDoughsListView.as_view(),name='cookies'),
    path('quizz/<int:waffel_id>/', views.waffles_quizz, name="waffles-quizz"),
    
]