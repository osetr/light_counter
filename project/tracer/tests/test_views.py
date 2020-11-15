from django.test import TestCase


class SearchFormTestCase(TestCase):
    def test_index_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_ajax_endpoint_from_not_ajax_req(self):
        response = self.client.get('/ajax/get_amount/')
        self.assertEqual(response.status_code, 404)

    def test_ajax_endpoint_from_ajax_req(self):
        response = self.client.get('/ajax/get_amount/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)