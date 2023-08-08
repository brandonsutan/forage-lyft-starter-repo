from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

    def engine_should_be_serviced(self):
        # Add your logic to determine if the Rorschach engine should be serviced based on other factors.
        # For example, you can check engine performance, mileage, or any other criteria specific to Rorschach engines.
        # Return True if the engine should be serviced; otherwise, return False.
        pass

