# Generated by Django 3.0.6 on 2020-05-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=3)),
                ('contextid', models.CharField(max_length=30)),
                ('classid', models.CharField(max_length=30)),
                ('icon_url', models.SlugField()),
                ('market_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='market',
            name='assetid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='market',
            name='classid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='market',
            name='contextid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='market',
            name='instanceid',
            field=models.CharField(max_length=30),
        ),
    ]
