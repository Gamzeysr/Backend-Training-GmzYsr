# Generated by Django 4.1.4 on 2022-12-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fscohort", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ["number"], "verbose_name_plural": "Student_list"},
        ),
    ]
