# Generated by Django 4.2.4 on 2023-09-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_application_interview'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='offer',
            field=models.CharField(choices=[('W', 'Awaiting'), ('C', 'Counter-offered'), ('R', 'Rejected'), ('A', 'Accepted')], default='W', max_length=1),
        ),
    ]
