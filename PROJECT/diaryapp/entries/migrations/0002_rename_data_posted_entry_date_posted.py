# Generated by Django 3.2.3 on 2021-06-11 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]