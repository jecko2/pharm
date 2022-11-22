# Generated by Django 4.1.3 on 2022-11-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_is_vetted_profile_is_cleared'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('WR', 'Writer'), ('ED', 'Editor')], default='WR', max_length=2),
        ),
    ]
