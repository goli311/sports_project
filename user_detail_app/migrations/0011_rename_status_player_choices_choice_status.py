# Generated by Django 4.0.3 on 2022-03-21 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail_app', '0010_player_choices_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player_choices',
            old_name='status',
            new_name='choice_status',
        ),
    ]
