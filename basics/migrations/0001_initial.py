# Generated by Django 3.2 on 2021-04-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('batch', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('cgpa', models.FloatField()),
                ('hsc', models.FloatField()),
                ('diploma', models.FloatField()),
                ('sslc', models.FloatField()),
                ('career', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=50)),
                ('placed', models.TextField(default='Nil')),
                ('status', models.CharField(default='not placed', max_length=50)),
            ],
        ),
    ]
