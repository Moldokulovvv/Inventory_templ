# Generated by Django 3.1 on 2021-04-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akts', '0003_akt_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akt',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]