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
[
 (52.2432783, 20.9680914),
 (52.2424119, 20.9696918),
 (52.2416544, 20.9701784),
 (52.2407996,  20.9705053),
 (52.2390884,  20.9711727),
 (52.2391056,  20.9712801),
 (52.2392296, 20.9753056),
 (52.2393807,  20.9764305)])

# {'y': 52.2395702, 'x': 20.9775679, 'osmid': 99404345, 'highway': 'traffic_signals'}
# {'y': 52.2382225, 'x': 20.9784095, 'osmid': 32912987, 'highway': 'traffic_signals'}
# {'y': 52.2380802, 'x': 20.9785409, 'osmid': 32912994, 'highway': 'traffic_signals'}
# {'y': 52.2372572, 'x': 20.9796644, 'osmid': 1118730317}
# {'y': 52.237044, 'x': 20.9799238, 'osmid': 32912944, 'highway': 'traffic_signals'}
# {'y': 52.2368319, 'x': 20.9800908, 'osmid': 32598967, 'highway': 'traffic_signals'}
# {'y': 52.2364853, 'x': 20.980199, 'osmid': 1118730216}
# {'y': 52.2355624, 'x': 20.980495, 'osmid': 190467928, 'highway': 'traffic_signals'}
# {'y': 52.2347524, 'x': 20.9809131, 'osmid': 1118730422}
# {'y': 52.2345769, 'x': 20.9810615, 'osmid': 32598961}
# {'y': 52.2332297, 'x': 20.9818964, 'osmid': 86970182, 'highway': 'traffic_signals'}
# {'y': 52.2304699, 'x': 20.9838533, 'osmid': 303205566}
# {'y': 52.2300165, 'x': 20.984241, 'osmid': 303205557}
# {'y': 52.2273212, 'x': 20.9867936, 'osmid': 30902341}
# {'y': 52.2260573, 'x': 20.9878155, 'osmid': 303205599}
# {'y': 52.2249954, 'x': 20.9885876, 'osmid': 32594631}
# {'y': 52.2249231, 'x': 20.9885898, 'osmid': 32594640}
# {'y': 52.2244124, 'x': 20.9889866, 'osmid': 32594637}
# {'y': 52.224007, 'x': 20.9895098, 'osmid': 3815213343}
# {'y': 52.223967, 'x': 20.9895602, 'osmid': 30902337}
# {'y': 52.2217031, 'x': 20.9896716, 'osmid': 54094223}
# {'y': 52.2206148, 'x': 20.9894977, 'osmid': 32572890}
# {'y': 52.2191255, 'x': 20.9893246, 'osmid': 30901480, 'highway': 'traffic_signals'}
# {'y': 52.2183917, 'x': 20.9890458, 'osmid': 248457778}
# {'y': 52.2183001, 'x': 20.9890036, 'osmid': 32606514}
# {'y': 52.2173923, 'x': 20.988572, 'osmid': 32048673}
# {'y': 52.2164922, 'x': 20.9881076, 'osmid': 30901479, 'highway': 'traffic_signals'}
# {'y': 52.2161788, 'x': 20.9880766, 'osmid': 30902333, 'highway': 'traffic_signals'}
# {'y': 52.2141155, 'x': 20.9883917, 'osmid': 32329841}
# {'y': 52.2103967, 'x': 20.9877491, 'osmid': 32049365, 'highway': 'traffic_signals'}
# {'y': 52.2102183, 'x': 20.9876789, 'osmid': 32049364}
# {'y': 52.2052718, 'x': 20.986011, 'osmid': 32605669, 'highway': 'traffic_signals'}
# {'y': 52.2012925, 'x': 20.9846204, 'osmid': 32605675, 'highway': 'traffic_signals'}
# {'y': 52.1985126, 'x': 20.9837265, 'osmid': 32049226, 'highway': 'traffic_signals'}
# {'y': 52.1984058, 'x': 20.9836798, 'osmid': 32049224, 'highway': 'traffic_signals'}
# {'y': 52.1942548, 'x': 20.9822667, 'osmid': 786449299, 'highway': 'traffic_signals'}
# {'y': 52.1914122, 'x': 20.981276, 'osmid': 253213099, 'highway': 'traffic_signals'}
# {'y': 52.1912902, 'x': 20.9812184, 'osmid': 32329945, 'highway': 'traffic_signals'}
# {'y': 52.1892287, 'x': 20.9805096, 'osmid': 316628084, 'highway': 'traffic_signals'}
# {'y': 52.1881849, 'x': 20.9801566, 'osmid': 316632610}
# {'y': 52.1837464, 'x': 20.978676, 'osmid': 26515511, 'highway': 'traffic_signals'}
# {'y': 52.1834345, 'x': 20.9785785, 'osmid': 26515509, 'highway': 'traffic_signals'}
# {'y': 52.1833181, 'x': 20.9789663, 'osmid': 26515507, 'highway': 'traffic_signals'}
# {'y': 52.1820622, 'x': 20.9831918, 'osmid': 1273140010}
# {'y': 52.1812841, 'x': 20.9844469, 'osmid': 1273140134}
# {'y': 52.1785244, 'x': 20.9859121, 'osmid': 1273140179}
# {'y': 52.1725, 'x': 20.9859543, 'osmid': 773638065, 'highway': 'motorway_junction'}
# {'y': 52.1641301, 'x': 20.9863714, 'osmid': 773638102}
# {'y': 52.1419264, 'x': 20.9886754, 'osmid': 1273027211, 'highway': 'motorway_junction'}
# {'y': 52.1412798, 'x': 20.9886625, 'osmid': 1273027279}
# {'y': 52.1391841, 'x': 20.9884006, 'osmid': 1273027164}
# {'y': 52.1380775, 'x': 20.9884376, 'osmid': 603030446}
# {'y': 52.1387528, 'x': 20.9913735, 'osmid': 1273027142}
# {'y': 52.1390616, 'x': 20.9996761, 'osmid': 1273027146}
# {'y': 52.139392, 'x': 21.0098699, 'osmid': 1273140109, 'highway': 'motorway_junction'}
# {'y': 52.1392484, 'x': 21.017227, 'osmid': 4876652623, 'highway': 'crossing'}
# {'y': 52.1392649, 'x': 21.0174505, 'osmid': 7770261218}
# {'y': 52.1392772, 'x': 21.0181306, 'osmid': 7770261219, 'highway': 'traffic_signals'}
# {'y': 52.1398814, 'x': 21.0182334, 'osmid': 1716473300}
# {'y': 52.1407033, 'x': 21.0180306, 'osmid': 32946688}
# {'y': 52.1417717, 'x': 21.0178476, 'osmid': 4068485282}
# {'y': 52.1435418, 'x': 21.0178237, 'osmid': 31930661, 'highway': 'traffic_signals'}
# {'y': 52.1436415, 'x': 21.0178205, 'osmid': 31718213, 'highway': 'traffic_signals'}
# {'y': 52.1447286, 'x': 21.0178183, 'osmid': 311426025}
# {'y': 52.1449482, 'x': 21.0180487, 'osmid': 339919510, 'highway': 'crossing'}
# {'y': 52.1449722, 'x': 21.0182426, 'osmid': 311426031}
# {'y': 52.1450206, 'x': 21.0182482, 'osmid': 8320862449}])