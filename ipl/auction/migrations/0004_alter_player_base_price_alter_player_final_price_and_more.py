# Generated by Django 5.0.4 on 2024-04-07 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_alter_player_final_price_alter_player_sold_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='base_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='final_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='funds_left',
            field=models.FloatField(),
        ),
    ]
