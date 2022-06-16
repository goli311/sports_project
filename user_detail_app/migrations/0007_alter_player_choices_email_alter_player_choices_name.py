# Generated by Django 4.0.3 on 2022-03-21 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail_app', '0006_alter_player_choices_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_choices',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_detail_app.user_details'),
        ),
        migrations.AlterField(
            model_name='player_choices',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_detail_app.players'),
        ),
    ]