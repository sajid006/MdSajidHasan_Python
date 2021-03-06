# Generated by Django 4.0 on 2021-12-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Pin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('WorkId', models.AutoField(primary_key=True, serialize=False)),
                ('DoorNo', models.IntegerField()),
                ('EmployeeId', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Type', models.IntegerField()),
                ('Pin', models.CharField(max_length=100)),
            ],
        ),
    ]
