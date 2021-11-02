from django.utils import timezone

from base.models import FakeModel
from base.test import BaseTestCase


class TestModelTest(BaseTestCase):
    def setUp(self):
        pass

    def validate_datetime_year_to_day(self, datetime1, datetime2):
        self.assertEqual(datetime1.year == datetime2.year, True)
        self.assertEqual(datetime1.month == datetime2.month, True)
        self.assertEqual(datetime1.day == datetime2.day, True)

    def test_create_test_model(self):
        test_dict = {
            'test': 'fake',
            'test2': 'fake2',
            'test3': 'fake3'
        }
        fake_model = FakeModel.objects.create(json=test_dict)
        created_date = timezone.now()
        last_modified_date = timezone.now()
        self.validate_datetime_year_to_day(fake_model.created_date, created_date)
        self.validate_datetime_year_to_day(fake_model.last_modified_date, last_modified_date)
        self.assertEqual(fake_model.json, test_dict)
