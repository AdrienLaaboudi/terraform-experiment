# Generated by Django 4.1.7 on 2023-03-16 20:29

from django.db import migrations, models
import registration_profile.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RegistrationProfile",
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
                (
                    "code",
                    models.CharField(
                        default=registration_profile.models.code_generator, max_length=5
                    ),
                ),
            ],
        ),
    ]
