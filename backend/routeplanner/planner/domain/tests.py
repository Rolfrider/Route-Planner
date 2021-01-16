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
        self.assertListEqual(a_star.find_path(( 52.2433443,  20.9681918), (52.2393807,  20.9764305)),

[(52.2432783, 20.9680914),
 (52.2424119, 20.9696918),
 (52.2416544, 20.9701784),
 (52.2407996,  20.9705053),
 (52.2390884,  20.9711727),
 (52.2391056,  20.9712801),
 (52.2392296, 20.9753056),
 (52.2393807,  20.9764305)])

    def testSamePoint(self):
            self.assertListEqual(a_star.find_path((52.2433443, 20.9681918), (52.2433443, 20.9681918)),

                                 [])

