# Generated by Django 3.0.6 on 2020-06-25 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200625_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='steamuser',
            name='authkey',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='steamuser',
            name='avatar',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='steamuser',
            name='avatarfull',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='steamuser',
            name='avatarmedium',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='steamuser',
            name='current_balance',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='profileurl',
            field=models.CharField(default='none', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='steamuser',
            name='tradeurl',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
