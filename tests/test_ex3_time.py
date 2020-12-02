import unittest
from unittest.mock import *
from ex3_time.checker import Checker
from ex3_time.environment import Environment
import datetime


class TestTime(unittest.TestCase):
    def test_remainder_success(self):
        test_object = Environment()
        test_object.get_time = Mock(name='get_time')
        test_object.get_time.return_value = datetime.datetime.strptime('17:05', '%H:%M')

        checker = Checker(test_object)
        checker.remainder()
        self.assertTrue(test_object.was_wav_played())

    def test_remainder_fail(self):
        test_object = Environment()
        test_object.get_time = Mock(name='get_time')
        test_object.get_time.return_value = datetime.datetime.strptime('16:54', '%H:%M')

        checker = Checker(test_object)
        checker.remainder()
        self.assertFalse(test_object.was_wav_played())

    def test_remainder_exactly_17(self):
        test_object = Environment()
        test_object.get_time = Mock(name='get_time')
        test_object.get_time.return_value = datetime.datetime.strptime('17:00', '%H:%M')

        checker = Checker(test_object)
        checker.remainder()
        self.assertTrue(test_object.was_wav_played())

    def test_remainder_reset(self):
        test_object = Environment()
        test_object.get_time = Mock(name='get_time')
        test_object.get_time.return_value = datetime.datetime.strptime('18:46', '%H:%M')

        checker = Checker(test_object)
        checker.remainder()
        test_object.reset_wav()
        self.assertFalse(test_object.was_wav_played())


if __name__ == '__main__':
    unittest.main()
