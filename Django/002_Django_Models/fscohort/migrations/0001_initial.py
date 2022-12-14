# Generated by Django 4.1.4 on 2022-12-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("number", models.IntegerField(default=1111)),
                ("about", models.TextField(blank=True, null=True)),
                ("register", models.DateTimeField(auto_now_add=True)),
                ("last_update_data", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField()),
            ],
        ),
    ]
