# Generated by Django 4.2.4 on 2023-09-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_alter_application_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='screening',
            field=models.CharField(choices=[('W', 'Awaiting'), ('A', 'Advancing'), ('R', 'Rejected')], default='W', max_length=1),
        ),
    ]
