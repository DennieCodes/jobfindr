# Generated by Django 4.2.4 on 2023-09-14 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_application_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_applied',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
