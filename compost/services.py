from compost.models import Measurement
import datetime

class RegisterMeasurement:
    def execute(self, measurement):
        now = datetime.datetime.now()
        Measurement.objects.create(temperature=measurement['temperature'], taken_at=now)
