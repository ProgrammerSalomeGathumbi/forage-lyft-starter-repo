class Car:
    def __init__(self, engine_service_required, battery_service_required):
        """
        Initialize a Car object with service requirements.

        Args:
            engine_service_required: shows if engine service is required.
            battery_service_required: shows if battery service is required.
        """
        self.engine_service_required = engine_service_required
        self.battery_service_required = battery_service_required

    def needservice(self):
        """
        Check if the car needs service.

        Returns:
            bool: True if service is required, False otherwise.
        """
        if self.engine_service_required or self.battery_service_required:
            return True
        else:
            return False
