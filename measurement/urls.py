from django.urls import path
from .views import CreateSensorView, ListSensorView, UpdateSensorView
from .views import CreateMeasurementView, SensorDetailView


urlpatterns = [
	# TODO: зарегистрируйте необходимые маршруты
	path("create_sensor/", CreateSensorView.as_view()),   
	path("list_sensors/", ListSensorView.as_view()),
	path("update_sensor/<pk>", UpdateSensorView.as_view()),
	path("add_temp/", CreateMeasurementView.as_view()),
	path("show/<pk>/", SensorDetailView.as_view()),
]
