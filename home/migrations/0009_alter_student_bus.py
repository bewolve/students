# Generated by Django 4.1.1 on 2022-09-24 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.bus'),
        ),
    ]
