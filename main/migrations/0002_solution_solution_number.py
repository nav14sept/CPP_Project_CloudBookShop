# Generated by Django 3.0.6 on 2020-05-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
