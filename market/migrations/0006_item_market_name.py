# Generated by Django 3.0.6 on 2020-06-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20200611_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='market_name',
            field=models.CharField(default='None', max_length=255),
            preserve_default=False,
        ),
    ]
