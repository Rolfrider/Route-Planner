from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
import json

def mocked_route_for(*args, **kwargs):
    return [{"lat": "12.12", "lng": "2.21"},  {"lat": "12.22", "lng": "11.21"}]
# Create your tests here.
@patch('planner.views.route_for', side_effect=mocked_route_for)
class PlannerIndexViewTests(TestCase):

    def test_request_no_body(self, route_for_mock):
        """
        Should return 400 - BAD REQUEST
        """
        response = self.client.get(reverse('planner:index'))
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "Request body can't be read"})
        self.assertFalse(route_for_mock.called)

    def test_request_with_wrong_body(self, route_for_mock):
        """
        Should return 400 - BAD REQUEST
        """
        invalid_request = '[{"wat": "12.12", "as": "2.21"},  {"as": "12.22", "lng": "11.21"}]'
        response = self.client.generic("GET", reverse('planner:index'), invalid_request, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, [
                {'lat': ['This field is required.'], 'lng': ['This field is required.']},
                {'lat': ['This field is required.']}
            ]
        )
        self.assertFalse(route_for_mock.called)
    
    def test_request_with_body(self, route_for_mock):
        """
        Should return 200 with json body
        """
        valid_request = '[{"lat": "12.12", "lng": "2.21"},  {"lat": "12.22", "lng": "11.21"}]'
        response = self.client.generic("GET", reverse('planner:index'), valid_request, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, mocked_route_for())
        self.assertTrue(route_for_mock.called)