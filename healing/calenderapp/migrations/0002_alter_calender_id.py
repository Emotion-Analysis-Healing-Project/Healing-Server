# Generated by Django 4.1 on 2022-08-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calenderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
