# Generated by Django 5.1 on 2024-09-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='course',
            field=models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development')], max_length=50),
        ),
    ]
