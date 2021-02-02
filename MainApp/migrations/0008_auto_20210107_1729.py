# Generated by Django 3.1 on 2021-01-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_auto_20210104_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
