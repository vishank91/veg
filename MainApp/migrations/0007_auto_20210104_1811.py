# Generated by Django 3.1 on 2021-01-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20210104_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='payOut',
            new_name='payOutTotal',
        ),
        migrations.AddField(
            model_name='member',
            name='gleftId',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='grightId',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='payWithdrawable',
            field=models.IntegerField(default=0),
        ),
    ]
