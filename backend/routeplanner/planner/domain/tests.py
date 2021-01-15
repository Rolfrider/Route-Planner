from django.test import TestCase

#from .a_star import find_path
from . import a_star
from .router import find_nearest_index, sort_by_dist


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

class DistanceSortingTest(TestCase):

    def test_sorting(self):
        """
        Should sort places to be nearest to following
        """
        places = [(10.10, 10.10), (12.1, 12.1), (8.11, 8.11), (6.3, 6.4)]
        self.assertListEqual(
            sort_by_dist(places),
            [(10.10, 10.10), (8.11, 8.11), (6.3, 6.4), (12.1, 12.1)]
        )

    def test_when_places_empty(self):
        """
        Should throw IndexError
        """
        self.assertRaises(IndexError, sort_by_dist, [])

class AStarTest(TestCase):


    def test(self):
        self.assertListEqual(a_star.find_path(( 20.9681918, 52.2433443), (21.0182482, 52.1450206)),
[(21.022332	,52.163138), (21.022001	,52.162806), (21.020822,	52.161883), (21.020733	,52.161754), (21.021066,	52.161568)])