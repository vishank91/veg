# Generated by Django 3.1 on 2021-01-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0014_auto_20210124_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bankName',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='ifscCode',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]