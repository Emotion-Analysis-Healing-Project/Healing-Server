# Generated by Django 4.1 on 2022-08-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('facial', models.CharField(choices=[('G', 'good'), ('B', 'bad'), ('S', 'sad'), ('N', 'nervous')], max_length=1)),
            ],
        ),
    ]
