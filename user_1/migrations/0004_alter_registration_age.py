# Generated by Django 5.1.1 on 2024-09-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_1', '0003_booking_patients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
