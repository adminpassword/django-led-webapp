# Generated by Django 3.0.7 on 2020-07-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vertical', '0003_auto_20200715_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boulder',
            name='boulder_data',
            field=models.CharField(max_length=400),
        ),
    ]
