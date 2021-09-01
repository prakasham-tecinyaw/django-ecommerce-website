# Generated by Django 3.1.2 on 2021-06-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210625_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='phone',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
