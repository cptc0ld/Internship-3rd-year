# Generated by Django 3.0.6 on 2020-05-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steamid', models.CharField(max_length=17, unique=True)),
                ('personaname', models.CharField(max_length=255)),
                ('profileurl', models.CharField(max_length=300)),
                ('avatar', models.CharField(max_length=255)),
                ('avatarmedium', models.CharField(max_length=255)),
                ('avatarfull', models.CharField(max_length=255)),
                ('appid', models.CharField(max_length=3)),
                ('contextid', models.CharField(max_length=3)),
                ('assetid', models.CharField(max_length=3)),
                ('classid', models.CharField(max_length=10)),
                ('instanceid', models.CharField(max_length=10)),
                ('icon_url', models.SlugField()),
                ('market_name', models.CharField(max_length=255)),
                ('tradable', models.BooleanField()),
            ],
        ),
    ]
