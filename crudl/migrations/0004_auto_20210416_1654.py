# Generated by Django 3.2 on 2021-04-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudl', '0003_auto_20210416_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='cgpa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='diploma',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='hsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='placed',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='sslc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
