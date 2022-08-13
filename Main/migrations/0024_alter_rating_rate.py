# Generated by Django 4.0.4 on 2022-07-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0023_alter_rating_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(choices=[(0, 0), (1, 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='0', max_length=1),
        ),
    ]