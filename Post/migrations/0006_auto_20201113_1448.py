# Generated by Django 3.1.1 on 2020-11-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_auto_20201113_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
