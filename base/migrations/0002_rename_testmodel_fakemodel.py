# Generated by Django 3.2.7 on 2021-10-10 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestModel',
            new_name='FakeModel',
        ),
    ]