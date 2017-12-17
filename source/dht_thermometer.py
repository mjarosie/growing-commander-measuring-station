from measurement_source import MeasurementSource
import Adafruit_DHT

class DhtThermometer(MeasurementSource):
	def __init__(self, device_unique_name, gpio_pin):
		self.device_unique_name = device_unique_name
		self.gpio_pin = gpio_pin
		self.sensor_type = Adafruit_DHT.AM2302
		
	def get_reading(self, results_storage=None):
		# Try to grab a sensor reading.  Use the read_retry method which will retry up
		# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
		humidity, temperature = Adafruit_DHT.read_retry(self.sensor_type, self.gpio_pin)
		if results_storage is not None:
			results_storage[self.device_unique_name] = (humidity, temperature)
		return (humidity, temperature)