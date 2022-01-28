# Generated by Django 4.0.1 on 2022-01-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rok', '0006_resource_gems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('governor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('governor_id', models.CharField(blank=True, max_length=255, null=True)),
                ('power', models.CharField(blank=True, max_length=255, null=True)),
                ('kill_points', models.CharField(blank=True, max_length=255, null=True)),
                ('civilization', models.CharField(blank=True, max_length=255, null=True)),
                ('kingdom', models.CharField(blank=True, max_length=255, null=True)),
                ('alliance', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
