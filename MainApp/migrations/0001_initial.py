# Generated by Django 3.1 on 2020-12-30 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('payoutNormal', models.IntegerField()),
                ('payoutBoosted', models.IntegerField()),
                ('capping', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('adhar', models.CharField(default=None, max_length=20, null=True)),
                ('pan', models.CharField(default=None, max_length=20, null=True)),
                ('joiningData', models.DateTimeField(auto_now=True)),
                ('PairCompleteDate', models.DateTimeField()),
                ('leftChild', models.BooleanField(default=False)),
                ('rightChild', models.BooleanField(default=False)),
                ('parentId', models.IntegerField(default=None, null=True)),
                ('leftId', models.IntegerField(default=None, null=True)),
                ('rightId', models.IntegerField(default=None, null=True)),
                ('payOut', models.IntegerField(default=0, null=True)),
                ('mobile', models.CharField(max_length=20)),
                ('photo', models.ImageField(default=None, null=True, upload_to='images')),
                ('planDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.plan')),
            ],
        ),
    ]
