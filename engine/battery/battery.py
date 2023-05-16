from datetime import datetime


class Battery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self, service_interval):
        current_date = datetime.now()
        time_since_last_service = current_date - self.last_service_date
        months_since_last_service = time_since_last_service.days // 30

        if months_since_last_service >= service_interval:
            return True
        else:
            return False
