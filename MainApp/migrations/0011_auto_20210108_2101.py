# Generated by Django 3.1 on 2021-01-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_auto_20210107_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gpid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='reference',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
