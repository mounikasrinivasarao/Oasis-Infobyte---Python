# Generated by Django 4.1.7 on 2024-02-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculator", "0008_alter_calculateddata_bmi_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
