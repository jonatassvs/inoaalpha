from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('acoes/', views.AcaoListView.as_view(), name='acoes'),
  path('acao/<int:pk>', views.AcaoDetailView.as_view(), name='acao-detail'),
  path('acoesusuario/', views.AcaoUserView.as_view(), name='acao-user'),
  path('sobre/', views.about, name='about'),

  path('acaodono/criar/', views.CriarAcaoDono.as_view(), name='acaodono-criar'),
  path('acaodono/delete/', views.ApagarAcaoDono.as_view(), name='acaodono-delete'),
]