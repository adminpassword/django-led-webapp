# Generated by Django 3.0.7 on 2020-07-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vertical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boulder',
            name='boulder_creator',
            field=models.CharField(max_length=15),
        ),
    ]
