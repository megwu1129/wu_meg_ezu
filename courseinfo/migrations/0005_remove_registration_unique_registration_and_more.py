# Generated by Django 4.1 on 2023-02-22 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "courseinfo",
            "0004_alter_instructor_options_alter_registration_options_and_more",
        ),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="registration", name="unique_registration",
        ),
        migrations.AddConstraint(
            model_name="registration",
            constraint=models.UniqueConstraint(
                fields=("section", "student"), name="unique_registrationmi"
            ),
        ),
    ]