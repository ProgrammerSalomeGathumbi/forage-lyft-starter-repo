import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.engine import Engine
from datetime import datetime, timedelta


class CapuletEngineTest(unittest.TestCase):
    def test_needs_service(self):
        # Create an instance of CapuletEngine with current_mileage 50000
        # and last_service_mileage 20000
        engine = CapuletEngine(50000, 20000)
        # Test that needs_service() returns True
        self.assertTrue(engine.needs_service())
        # Update the instance with current_mileage 55000
        engine.current_mileage = 55000
        # Test that needs_service() still returns True
        self.assertTrue(engine.needs_service())
        # Update the instance with current_mileage 70000
        engine.current_mileage = 70000
        # Test that needs_service() now returns False
        self.assertFalse(engine.needs_service())


class SternmanEngineTest(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.now()
        last_service_date = current_date - timedelta(days=180)
        # Instance with warning light on and last service date
        engine = SternmanEngine(True, last_service_date)
        # Test that needs_service() returns True
        self.assertTrue(engine.needs_service())
        last_service_date = current_date - timedelta(days=365)
        # Instance with warning light off and last service date
        engine = SternmanEngine(False, last_service_date)
        # Test that needs_service() returns False
        self.assertFalse(engine.needs_service())


class WilloughbyEngineTest(unittest.TestCase):
    def test_needs_service(self):
        # Create an instance of WilloughbyEngine with current_mileage 50000
        # and last_service_mileage 20000
        engine = WilloughbyEngine(50000, 20000)
        # Test that needs_service() returns True
        self.assertTrue(engine.needs_service())
        # Update the instance with current_mileage 70000
        engine.current_mileage = 70000
        # Test that needs_service() now returns True
        self.assertTrue(engine.needs_service())
        # Update the instance with current_mileage 80000
        engine.current_mileage = 80000
        # Test that needs_service() still returns True
        self.assertTrue(engine.needs_service())
        # Update the instance with current_mileage 10000
        engine.current_mileage = 10000
        # Test that needs_service() now returns False
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
