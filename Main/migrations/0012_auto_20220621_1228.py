# Generated by Django 3.0.5 on 2022-06-21 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20220617_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinator',
            name='coid',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='mail',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mail',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='ta',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.course'),
        ),
    ]
