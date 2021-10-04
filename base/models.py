from django.db import models
from django.db.models import DateTimeField


class TestModel(models.Model):
    created_date = DateTimeField(auto_now=True)
    last_modified_date = DateTimeField(auto_now=True)
