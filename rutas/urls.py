from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('panel/', views.panel_control, name='panel_control'),
    path('panel/nueva/', views.crear_ruta, name='crear_ruta'),
    path('panel/editar/<int:pk>/', views.editar_ruta, name='editar_ruta'),   # <-- NUEVA
    path('panel/eliminar/<int:pk>/', views.eliminar_ruta, name='eliminar_ruta'),
]