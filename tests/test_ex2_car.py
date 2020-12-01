import unittest
from unittest.mock import *
from ex2_car.car import Car
from ex2_car.engine import Engine


class TestCar(unittest.TestCase):
    @patch.object(Car, 'needsFuel')
    def test_needsFuel(self, mock_method):
        mock_method.return_value = False
        car = Car()
        self.assertFalse(car.needsFuel())

    @patch.object(Car, 'driveTo')
    def test_driveTo(self, mock_method):
        mock_method.side_effect = lambda x: 'Driving to ' + x
        car = Car()

        city = 'Warsaw'
        self.assertEqual(car.driveTo(city), 'Driving to ' + city)

    @patch.object(Engine, 'getTemperature')
    def test_getEngineTemperature(self, mock_method):
        mock_method.return_value = 40
        engine = Engine()
        car = Car(engine)
        self.assertEqual(car.getEngineTemperature(), 40)


if __name__ == '__main__':
    unittest.main()
