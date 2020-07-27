# Generated by Django 3.0.7 on 2020-07-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boulder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boulder_description', models.CharField(max_length=300)),
                ('boulder_difficulty', models.CharField(max_length=100)),
                ('boulder_creator', models.CharField(max_length=10)),
                ('boulder_name', models.CharField(max_length=50)),
                ('boulder_data', models.CharField(max_length=200)),
            ],
        ),
    ]
