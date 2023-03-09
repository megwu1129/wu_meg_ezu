# Generated by Django 4.1 on 2023-02-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courseinfo", "0002_alter_course_options_course_unique_course"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="period", options={"ordering": ["period_sequence"]},
        ),
        migrations.AlterModelOptions(
            name="semester",
            options={"ordering": ["year__year", "period__period_sequence"]},
        ),
        migrations.AlterModelOptions(name="year", options={"ordering": ["year"]},),
        migrations.RenameField(
            model_name="semester", old_name="period_id", new_name="period",
        ),
        migrations.RenameField(
            model_name="semester", old_name="year_id", new_name="year",
        ),
        migrations.AddConstraint(
            model_name="semester",
            constraint=models.UniqueConstraint(
                fields=("year", "period"), name="unique_semester"
            ),
        ),
    ]