# Generated by Django 3.1 on 2021-01-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0017_remove_member_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='childId',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]