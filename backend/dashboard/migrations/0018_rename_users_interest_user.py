# Generated by Django 4.0.3 on 2022-05-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_remove_interest_users_interest_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interest',
            old_name='users',
            new_name='user',
        ),
    ]
