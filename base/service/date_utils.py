from django.utils import dateparse, timezone


def convert_datetime2localtime(dt):
    if not timezone.is_aware(dt):
        dt = timezone.make_aware(dt)
    return timezone.localtime(dt)


def convert_str2datetime(date_str, hh_mm_ss='00:00:00'):
    if not date_str:
        return None

    if type(date_str) is not str or type(hh_mm_ss) is not str:
        return None

    date_str += f' {hh_mm_ss}'
    dt = dateparse.parse_datetime(date_str)
    if not dt:
        raise Exception(f'{date_str} 는 유효한 값이 아닙니다.')
    return convert_datetime2localtime(dt)
