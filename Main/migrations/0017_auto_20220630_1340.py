# Generated by Django 3.0.5 on 2022-06-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0016_auto_20220630_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='cid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Main.course'),
        ),
    ]
