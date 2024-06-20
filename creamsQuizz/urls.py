from django.urls import path # type: ignore
from . import views
app_name = 'quizz'
urlpatterns = [
    path('', views.index, name="index"),
    #Lists of desserts names
    path('waffels/',views.WaffelListView.as_view(),name='waffels'),
    path('crepes/',views.CrepesListView.as_view(),name='crepes'),
    path('cookies/',views.CookieDoughsListView.as_view(),name='cookies'),
    #path('waffels/<int:pk>/',views.WaffelDetailView.as_view(),name='waffel-detail'),
    path('waffels/<int:waffel_id>/',views.waffel_detail,name='waffel-detail'),
    path('waffels/<int:waffel_id>/vote/',views.waffel_vote,name='waffel-vote'),
    path('waffel/<int:pk>/result/', views.WaffelResultView.as_view(), name='waffel-result'),

    
]
