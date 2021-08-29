from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<int:pk_p>/', views.get_measurement_by_id, name='measurementList'),
    path('<int:pk_p>/delete', views.delete_measurement_by_id, name='measurementList'),
    path('<int:pk_p>/update/<str:name_value_p>/<slug:new_value_p>', views.update_measurement_by_id
         , name='measurementList'),
]