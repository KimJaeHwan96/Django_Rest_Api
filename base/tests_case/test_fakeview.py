from base.models import FakeModel
from base.test import BaseTestCase


class GenericViewTest(BaseTestCase):
    def setUp(self):
        self.fake_model = FakeModel.objects.create()

    def test_get_fake_model_view(self):
        fake_model = self.fake_model
        self.get(f'/fake-models/{fake_model.id}/')
        self.response_200()
        response = self.last_response.json()
        self.assertEqual(fake_model.created_date.strftime('%Y-%m-%d %H:%M:%S'), response['created_date'])
        self.assertEqual(fake_model.last_modified_date.strftime('%Y-%m-%d %H:%M:%S'), response['last_modified_date'])

    def test_get_fake_model_all_view(self):
        fake_model = self.fake_model
        self.get(f'/fake-models/')
        self.response_200()
        response = self.last_response.json()[0]
        self.assertEqual(fake_model.created_date.strftime('%Y-%m-%d %H:%M:%S'), response['created_date'])
        self.assertEqual(fake_model.last_modified_date.strftime('%Y-%m-%d %H:%M:%S'), response['last_modified_date'])

    def test_post_fake_model_view(self):
        self.post('/fake-models/', data={})
        self.response_201()
        response = self.last_response.json()
        self.assertIn('id', response)
        self.assertIn('created_date', response)
        self.assertIn('last_modified_date', response)

    def test_put_fake_model_view(self):
        fake_model = self.fake_model
        self.put(f'/fake-models/{fake_model.id}/', data={'id': fake_model.id + 1})
        self.response_200()
        response = self.last_response.json()
        self.assertEqual(fake_model.id + 1, response['id'])

    def test_delete_fake_model_view(self):
        fake_model = self.fake_model
        self.delete(f'/fake-models/{fake_model.id}/')
        self.response_204()
        with self.assertRaises(FakeModel.DoesNotExist):
            fake_model.refresh_from_db()
