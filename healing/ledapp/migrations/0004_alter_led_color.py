# Generated by Django 4.1 on 2022-08-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledapp', '0003_alter_led_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='led',
            name='color',
            field=models.CharField(choices=[('r', 'red'), ('b', 'blue'), ('g', 'green'), ('y', 'yellow')], max_length=1),
        ),
    ]
