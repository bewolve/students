# Generated by Django 4.1.1 on 2022-09-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bus_student_gender_student_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='driver_number',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bus',
            name='driver_name',
            field=models.CharField(max_length=150),
        ),
    ]