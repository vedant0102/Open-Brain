# Generated by Django 3.2.8 on 2021-11-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]