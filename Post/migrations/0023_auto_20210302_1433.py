# Generated by Django 3.1.1 on 2021-03-02 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0022_auto_20210302_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='backsideview',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='frontview',
            new_name='image2',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='leftsideview',
            new_name='image3',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='rightsideview',
            new_name='image4',
        ),
    ]
