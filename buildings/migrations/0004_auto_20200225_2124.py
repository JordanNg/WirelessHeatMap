# Generated by Django 3.0.2 on 2020-02-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_auto_20200219_2316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='floor',
            options={'ordering': ['building', 'number']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['building', 'floor', 'number']},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='baseline',
            new_name='baseline_clients',
        ),
        migrations.AddField(
            model_name='room',
            name='baseline_bandwidth',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='building',
            name='render',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='remder',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='room',
            name='render',
            field=models.TextField(default='None'),
        ),
    ]
