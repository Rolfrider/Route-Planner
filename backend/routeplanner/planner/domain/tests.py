from django.test import TestCase
from .router import find_nearest_index


class NearestIndexTest(TestCase):

    def test_when_places_are_the_same(self):
        """
        When places contains only one elemnet which is the
        same as origin place should return index 0
        """
        index = find_nearest_index((12.12, 13.13), [(12.12, 13.13)])
        self.assertEqual(index, 0)

    def test_when_places_are_empty(self):
        """
        Should throw IndexError
        """
        self.assertRaises(IndexError, find_nearest_index, (12.12, 13.13), [])

    def test_returns_nearest_index(self):
        """
        Should return index 0
        """
        index = find_nearest_index((12.12, 13.13), [(12.14, 13.14), (23.11, 55.23)])
        self.assertEqual(index, 0)