from datetime import datetime

from django.utils import timezone, dateparse

from base.service.date_utils import convert_str2datetime, convert_datetime2localtime
from base.test import BaseTestCase


class DateUtilsTest(BaseTestCase):
    def test_convert_datetime2localtime(self):
        set_time = datetime(year=2021, month=10, day=30, hour=0, minute=0, second=0)
        set_time = timezone.make_aware(set_time)
        set_time = timezone.localtime(set_time)

        local_time = convert_datetime2localtime(set_time)
        self.assertEqual(set_time, local_time)

    def test_convert_str2datetime(self):
        set_time = datetime(year=2021, month=10, day=30, hour=0, minute=0, second=0)
        local_time = convert_datetime2localtime(set_time)

        now_time = convert_str2datetime('2021-10-30')
        self.assertEqual(local_time, now_time)

    def test_convert_str2datetime_with_hh_mm_ss(self):
        set_time = datetime(year=2021, month=10, day=30, hour=20, minute=21, second=15)
        local_time = convert_datetime2localtime(set_time)

        now_time = convert_str2datetime('2021-10-30', '20:21:15')
        self.assertEqual(local_time, now_time)
