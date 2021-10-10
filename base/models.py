from django.db import models
from django.db.models import DateTimeField

from base.manager import BaseManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = DateTimeField(auto_now=True)
    last_modified_date = DateTimeField(auto_now=True)


class FakeModel(BaseModel):
    objects = BaseManager()
