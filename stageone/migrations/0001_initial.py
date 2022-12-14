# Generated by Django 4.1.2 on 2022-10-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StageOneUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=50, verbose_name='slack username')),
                ('backend', models.BooleanField(default=True, verbose_name='backend user')),
                ('age', models.PositiveSmallIntegerField(verbose_name='user age')),
                ('bio', models.TextField(verbose_name='description about yourself')),
            ],
        ),
    ]
