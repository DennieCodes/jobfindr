# Generated by Django 4.2.4 on 2023-09-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0011_application_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='interview',
            field=models.CharField(choices=[('W', 'Awaiting'), ('O', 'On-going'), ('P', 'Passed'), ('R', 'Rejected')], default='W', max_length=1),
        ),
    ]
