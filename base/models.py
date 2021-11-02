from django.db import models
from django.db.models import DateTimeField, JSONField

from base.manager import BaseManager


class TimeStamp(models.Model):
    class Meta:
        abstract = True

    created_date = DateTimeField(auto_now=True)
    last_modified_date = DateTimeField(auto_now_add=True)


class JsonColumn(models.Model):
    class Meta:
        abstract = True

    json = JSONField(blank=True, null=True)


class BaseModel(TimeStamp, JsonColumn):
    class Meta:
        abstract = True


class FakeModel(BaseModel):
    objects = BaseManager()
