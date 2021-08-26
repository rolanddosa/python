import unittest

from Car import Car


class FirstUnitTest(unittest.TestCase):

    def test_set_up(self):
        pass

    def test_should_get_property_of_object(self):  # remember to name test methods starting with 'test_'
        # Assume
        car = Car(10)

        # Action
        property_to_test = car.speed

        # Assert
        self.assertEqual(property_to_test, 10)
