# Generated by Django 4.2.17 on 2025-01-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_alter_userpreference_bio_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='bio_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
