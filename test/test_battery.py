import unittest
from datetime import datetime, timedelta
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class NubbinBatteryTest(unittest.TestCase):
    def setUp(self):
        # Create an instance with last service date of one year ago
        self.nubbin = NubbinBattery(datetime.now(),
                                    datetime.now() - timedelta(days=365))

    def test_needs_service_when_service_is_needed(self):
        # Instance with the current 4 years ahead of the last service date
        self.nubbin.current_date = self.nubbin.last_service_date \
                                   + timedelta(days=1460)
        # Test that needs_service() returns True
        self.assertTrue(self.nubbin.needs_service())

    def test_needs_service_when_service_is_not_needed(self):
        # Instance with the current 2 years ahead of the last service date
        self.nubbin.current_date = self.nubbin.last_service_date \
                                   + timedelta(days=730)
        # Test that needs_service() returns False
        self.assertFalse(self.nubbin.needs_service())


class SpindlerBatteryTest(unittest.TestCase):
    def setUp(self):
        # Instance of SpindlerBattery with last service date of 6 months ago
        self.spindler = SpindlerBattery(datetime.now(),
                                        datetime.now() - timedelta(days=180))

    def test_needs_service_when_service_is_needed(self):
        # Instance with the current 2 years ahead of the last service date
        self.spindler.current_date = self.spindler.last_service_date \
                                     + timedelta(days=730)
        # Test that needs_service() returns True
        self.assertTrue(self.spindler.needs_service())

    def test_needs_service_when_service_is_not_needed(self):
        # Instance with the current 1 year ahead of the last service date
        self.spindler.current_date = self.spindler.last_service_date \
                                     + timedelta(days=365)
        # Test that needs_service() returns False
        self.assertFalse(self.spindler.needs_service())


if __name__ == '__main__':
    unittest.main()
