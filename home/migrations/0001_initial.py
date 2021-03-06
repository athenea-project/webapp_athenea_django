# Generated by Django 2.1.dev20180127235140 on 2018-01-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('profesorEmail', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
