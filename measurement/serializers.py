from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = ['id', 'name', 'description']
		
class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ['sensor_id','temperature','measure_date']
		
		
class MASerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ['temperature','measure_date']
	
		
class SensorDetailSerializer(serializers.ModelSerializer):
	measurements = MASerializer(read_only=True, many=True)
	class Meta:
		model = Sensor
		fields = ['id', 'name', 'description', 'measurements']
