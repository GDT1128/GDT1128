# Generated by Django 4.2.15 on 2024-09-02 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("insurance_date", "0005_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="User", new_name="EndUser",),
    ]
