import unittest
from unittest.mock import *
from ex2_car.car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    @patch.object(Car, 'needsFuel')
    def test_needsFuel(self, mock_method):
        mock_method.return_value = False
        self.assertFalse(self.car.needsFuel())

    @patch.object(Car, 'driveTo')
    def test_driveTo(self, mock_method):
        mock_method.side_effect = lambda x: 'Driving to ' + x

        city = 'Warsaw'
        self.assertEqual(self.car.driveTo(city), 'Driving to ' + city)

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature(self, mock_method):
        mock_method.return_value = 40
        self.assertEqual(self.car.getEngineTemperature(), 40)

    def tearDown(self):
        self.car = None


if __name__ == '__main__':
    unittest.main()
