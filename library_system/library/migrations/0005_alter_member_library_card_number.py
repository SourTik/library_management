# Generated by Django 5.2 on 2025-05-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='library_card_number',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
