# Generated by Django 3.2.3 on 2021-06-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constructor_name', models.CharField(max_length=50)),
                ('base', models.CharField(max_length=100)),
                ('team_chief', models.CharField(max_length=30)),
                ('first_team_entry', models.IntegerField()),
                ('pole_positions', models.IntegerField()),
            ],
        ),
    ]