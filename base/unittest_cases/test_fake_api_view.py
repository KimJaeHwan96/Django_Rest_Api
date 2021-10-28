from base.models import FakeModel
from base.test import BaseTestCase


class GenericViewTest(BaseTestCase):
    """
    APIView class 에 대한 테스트 케이스
    """
    def setUp(self):
        self.fake_model = FakeModel.objects.create()

    def test_get_fake_model_view(self):
        fake_model = self.fake_model
        self.get(f'/fake-models-for-api-view/{fake_model.id}/')
        self.response_200()

    def test_get_fake_model_view_query_string(self):
        self.get('/fake-models-for-api-view/?created_date=2021-10-24')
        self.response_200()

    def test_post_fake_model_view(self):
        self.post('/fake-models-for-api-view/')
        self.response_403()
