# Generated by Django 4.1.7 on 2023-03-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customauth", "0005_useraccount_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="usermoney",
            field=models.IntegerField(default=1000000),
        ),
    ]
