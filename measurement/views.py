# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
#from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

from django.http import HttpResponse

class CreateSensorView(CreateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer
	
class ListSensorView(ListCreateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer

class UpdateSensorView(RetrieveUpdateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer
	
class CreateMeasurementView(CreateAPIView):
	queryset = Measurement.objects.all()
	serializer_class = MeasurementSerializer

class SensorDetailView(RetrieveUpdateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorDetailSerializer

