from django.test import TestCase
from django.utils import timezone

from base.models import TestModel


def validate_datetime_year_to_day(datetime1, datetime2):
    assert datetime1.year == datetime2.year
    assert datetime1.month == datetime2.month
    assert datetime1.day == datetime2.day


# unittest.TestCase --(상속)-> django.test.SimpleTestCase --(상속)-> django.test.TransactionTestCase --(상속)-> django.test.TestCase
class Test(TestCase):
    def test_create_test_model(self):
        test_model = TestModel()
        test_model.save()
        created_date = timezone.now()
        last_modified_date = timezone.now()
        validate_datetime_year_to_day(test_model.created_date, created_date)
        validate_datetime_year_to_day(test_model.last_modified_date, last_modified_date)
